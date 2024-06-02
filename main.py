from PIL import Image, ImageEnhance, ImageFilter
import os

# Define the paths for the original images and the output directory
path = '/home/emmanuel/Documents/image editor/originals'
path_out = '/edited'

# Loop through each file in the specified directory
for filename in os.listdir(path):
    # Construct the full file path
    file_path = f"{path}/{filename}"
    
    # Open the image file
    img = Image.open(file_path)
    
    # Apply the SHARPEN filter, convert to grayscale, and apply the BLUR filter
    edit = img.filter(ImageFilter.SHARPEN).convert('L').filter(ImageFilter.BLUR)

    # Define the enhancement factor for contrast adjustment
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    # Apply the contrast enhancement
    edit = enhancer.enhance(factor)
    
    # Extract the base name of the file (without extension)
    clean_name = os.path.splitext(filename)[0]

    # Save the edited image to the output directory with a new name
    # Ensure the output directory exists
    if not os.path.exists(f'.{path_out}'):
        os.makedirs(f'.{path_out}')
    
    # Save the edited image
    edit.save(f'.{path_out}/{clean_name}_edited.jpg')

    # Print a message indicating the file has been processed
    print(f"Processed and saved: {clean_name}_edited.jpg")
