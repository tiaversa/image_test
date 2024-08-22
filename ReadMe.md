# Specify the image section with most white area

### What this is:
This is a python script with a container to run an test multiple images at the same time. It is a rudimental process
that was created to support in the utilizetion of other teams.

### What this isn't:
A full fledged application that is highly interactive.

## SetUp:
To run this project it is helpfull to have docker installed in your machine but not required. If you don't have docker
please run the following code into your machine's terminal for set up.
```
pip install -r requirements.txt
```

## How to utilize this code:
1. Download the code to your machine.
2. Add the images to be processes in the images folder.
3. Run the python script.
```
python3 image_testing.py <optional -i "image_name">
```

## Result:
1. Printed statements on the terminal.
```
Image image (3).png has more open space on section middle-left.
Image image (2).png has more open space on section top-left.
Image image (1).png has more open space on section bottom-right.
```
2. A CSV file with the report (see example in the project), with the following:
- File name.
- The name of the section with the most white space (e.g., 'top-left', 'middle-center', 'bottom-right')
- The coordinates of that section

## What it does:
- It divides the image into nine sections using horizontal and vertical thirds.
- It counts the number of white pixels (pixel value 255) in each section.
- It determines which section has the most white pixels.
- It calculates the coordinates (x_start, y_start, x_end, y_end) for the section with the most white pixels.