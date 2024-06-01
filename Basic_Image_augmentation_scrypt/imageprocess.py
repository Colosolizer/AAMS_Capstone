import os
import uuid
from PIL import Image


# Set the input and output folders
input_folder = 'F:/Documentz/AAMS/Fisheye/Goldfish_images_unprocessed_unlabeled'
output_folder = 'F:/Documentz/AAMS/Fisheye/goldfish_large_rotate'

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
        image = image.resize((1280, 720))
        
        
        # Calculate the size of each grid
        #grid_width = 320
        #grid_height = 180
        grid_width = 640
        grid_height = 360
        
        # Loop through each grid position
        for row in range(2):
            for col in range(2):
                # Calculate the coordinates of the current grid
                left = col * grid_width
                top = row * grid_height
                right = left + grid_width
                bottom = top + grid_height
                
                # Crop the image to the current grid
                grid_image = image.crop((left, top, right, bottom))
                grid_image = image.rotate(270)
                
               

                # Save the grid image to the output folder
                #grid_filename = f'{os.path.splitext(filename)[0]}_row{row}_col{col}.png'
                grid_filename = f'{os.path.splitext(filename)[0]}_row{row}_col{col}_large_rotate.png'
                grid_path = os.path.join(output_folder, grid_filename)
                grid_image.save(grid_path)