import os, argparse
from PIL import Image
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(
    description=("Find the area with more white spaces in the image.")
)
parser.add_argument("--image_path", "-i", help="Name of the image.",type=str, default="")

def test_image(image_name):
    # Load the image
    img = Image.open(f'images/{image_name}')

    # Convert the image to grayscale
    gray_img = img.convert('L')

    # Convert the grayscale image to a numpy array
    np_img = np.array(gray_img)

    # Get image dimensions
    height, width = np_img.shape

    # Define section boundaries
    h_thirds = [height // 3, 2 * height // 3]
    w_thirds = [width // 3, 2 * width // 3]

    # Initialize counters for each section
    sections = {
        'top-left': 0, 'top-center': 0, 'top-right': 0,
        'middle-left': 0, 'middle-center': 0, 'middle-right': 0,
        'bottom-left': 0, 'bottom-center': 0, 'bottom-right': 0
    }

    # Count white pixels in each section
    for y in range(height):
        for x in range(width):
            if np_img[y, x] == 255:  # Check for white pixels
                if y < h_thirds[0]:
                    if x < w_thirds[0]:
                        sections['top-left'] += 1
                    elif x < w_thirds[1]:
                        sections['top-center'] += 1
                    else:
                        sections['top-right'] += 1
                elif y < h_thirds[1]:
                    if x < w_thirds[0]:
                        sections['middle-left'] += 1
                    elif x < w_thirds[1]:
                        sections['middle-center'] += 1
                    else:
                        sections['middle-right'] += 1
                else:
                    if x < w_thirds[0]:
                        sections['bottom-left'] += 1
                    elif x < w_thirds[1]:
                        sections['bottom-center'] += 1
                    else:
                        sections['bottom-right'] += 1

    # Find the section with the most white pixels
    whitest_section = max(sections, key=sections.get)

    # Calculate coordinates for the whitest section
    if whitest_section.startswith('top'):
        y_start, y_end = 0, h_thirds[0]
    elif whitest_section.startswith('middle'):
        y_start, y_end = h_thirds[0], h_thirds[1]
    else:
        y_start, y_end = h_thirds[1], height

    if whitest_section.endswith('left'):
        x_start, x_end = 0, w_thirds[0]
    elif whitest_section.endswith('center'):
        x_start, x_end = w_thirds[0], w_thirds[1]
    else:
        x_start, x_end = w_thirds[1], width

    coordinates = (x_start, y_start, x_end, y_end)

    return whitest_section, coordinates
    
if __name__ == '__main__':
    df = pd.DataFrame(columns=['image', 'location', 'coordinates'])
    args = parser.parse_args()
    if not args.image_path == "":
        location, coords = test_image(args.image_path)
        print(f"Image {args.image_path} has more open space on section {location}.")
        df.loc[len(df.index)] = [args.image_path, location, coords] 
    else:
        image_list = os.listdir('./images')
        for image in image_list:
            location, coords = test_image(image)
            print(f"Image {image} has more open space on section {location}.")
            df.loc[len(df.index)] = [image, location, coords] 
    df.to_csv('images_report.csv', index=False)