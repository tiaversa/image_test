import os, argparse
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(
    description=("Find the area with more white spaces in the image.")
)
parser.add_argument("--image_path", "-ip", help="Table to be transfered.",type=str, default="")


def test_image(image_name):
    # Load the image
    img = Image.open(image_name)

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

    # Place your text
    if product_location == 'top':
        print(f"Image: {image_name} has more open space on Top")
        pass
    else:
        print(f"Image: {image_name} has more open space on Bottom")
        pass

if __name__ == '__main__':
    args = parser.parse_args()
    if not args.image_path == "":
        test_image(args.image_path)
    else:
        image_list = os.listdir('./images')
        for image in image_list:
            test_image(f'images/{image}')