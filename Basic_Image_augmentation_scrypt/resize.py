import os
from PIL import Image


# Set the input and output folders
input_folder = 'F:/Documentz/AAMS/Fisheye/goldfish_largeimage'
output_folder = 'F:/Documentz/AAMS/Fisheye/Goldfish_yolo_resize_big'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # Resize the image to 1280 x 720 pixels
        image = image.resize((416, 416))
        
        
                
               

        # Save the grid image to the output folder
        #grid_filename = f'{os.path.splitext(filename)[0]}_row{row}_col{col}.png'
        image_filename = f'{os.path.splitext(filename)[0]}_resized.png'
        image_path = os.path.join(output_folder, image_filename)
        image.save(image_path)