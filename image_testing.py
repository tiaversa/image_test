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

    # Identify non-white pixels
    non_white_pixels = np.where(np_img < 255)

    # Determine the location of non-white pixels
    y_coordinates = non_white_pixels[0]
    x_coordinates = non_white_pixels[1]

    # Determine the area with the most non-white pixels
    product_location = 'top' if np.mean(y_coordinates) > np_img.shape[0] / 2 else 'bottom'

    return product_location
    # Place your text
    

if __name__ == '__main__':
    df = pd.DataFrame(columns=['image', 'section'])
    args = parser.parse_args()
    if not args.image_path == "":
        product_location = test_image(args.image_path)
        print(f"Image {args.image_path} has more open space on {product_location}.")
        df.loc[len(df.index)] = [args.image_path, product_location] 
    else:
        image_list = os.listdir('./images')
        for image in image_list:
            product_location = test_image(image)
            print(f"Image {image} has more open space on {product_location}.")
            df.loc[len(df.index)] = [image, product_location] 
    df.to_csv('images_report.csv', index=False)