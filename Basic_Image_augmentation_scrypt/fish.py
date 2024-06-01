import inference
import os
import stat


model = inference.get_model("goldfish-detection/1")
model.infer(image = 'photo_2024-05-18_22-57-27_row1_col1_large_resized.png')
