from flask import Flask, Response, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from roboflow import Roboflow
import threading
import serial

app = Flask(__name__)
CORS(app)

# Initialize Roboflow
rf = Roboflow(api_key="CKR9tNCfpEUAyojAw3Zk")
project = rf.workspace().project("goldfish-detection")
model = project.version(2).model

# Global variable to store the latest predictions
latest_predictions = []

# Lock for thread-safe updates to the latest_predictions
predictions_lock = threading.Lock()

def gen_frames():
    cap = cv2.VideoCapture(0)  # Use the Raspberry Pi camera module
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Convert frame to image file for Roboflow
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Save the frame to a file (temporarily)
            with open("temp_frame.jpg", "wb") as f:
                f.write(frame_bytes)

            # Run Roboflow inference on the saved frame
            predictions = model.predict("temp_frame.jpg", confidence=40, overlap=30).json()

            # Update the global latest_predictions
            with predictions_lock:
                latest_predictions = predictions['predictions']

            # Draw bounding boxes on the frame
            for prediction in predictions['predictions']:
                x0 = int(prediction['x'] - prediction['width'] // 2)
                y0 = int(prediction['y'] - prediction['height'] // 2)
                x1 = int(prediction['x'] + prediction['width'] // 2)
                y1 = int(prediction['y'] + prediction['height'] // 2)

                cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                cv2.putText(frame, prediction['class'], (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            # Convert frame back to JPEG for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/num_fish')
def num_fish():
    with predictions_lock:
        num_fish = len(latest_predictions)
    return jsonify({'num_fish': num_fish})


@app.route('/cond')
def cond():
    ser = serial.Serial('/dev/ttyS0', 9600)  # open serial port
    while True:
        received_data = ser.read()  # read serial port
        data_left = ser.inWaiting()  # check for remaining byte
        received_data += ser.read(data_left)
        
        if received_data:
            print(received_data)  # print received data
            ser.write(received_data)  # transmit data serially
        return jsonify({'cond': cond})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
