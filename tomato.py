from os.path import isfile
from sys import path
import cv2
import numpy as np
import os

prices = {
        "Good" : 1000,
        "Edible" : 800,
        "InEdible" : 300
        }
qualities = {
        "Good" : [],
        "Edible" : [],
        "InEdible" : []
        }
def classify_quality(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None: 
        print(f"Could not open or find the image : {image_path}")
        return

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red, yellow, and green in HSV
    red_lower1 = np.array([0, 100, 100])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])
    red_upper2 = np.array([180, 255, 255])

    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    green_lower = np.array([35, 100, 100])
    green_upper = np.array([85, 255, 255])

    # Create masks for the colors
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    # Determine the color of the tomato based on the largest area of color detected
    red_count = cv2.countNonZero(red_mask)
    yellow_count = cv2.countNonZero(yellow_mask)
    green_count = cv2.countNonZero(green_mask)

    if red_count > yellow_count and red_count > green_count:
        text = "Good"
        qualities["Good"].append(image_path)
    elif yellow_count > red_count and yellow_count > green_count:
        text = "Edible"
        qualities["Edible"].append(image_path)
    else:
        text = "Inedible"
        qualities["InEdible"].append(image_path)

    # Put the text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the image
    cv2.imshow("Tomato Classification", image)
    while True:
        key = cv2.waitKey(0)
        if key == ord(' '):
            break
    cv2.destroyAllWindows()

# Example usage


def display():

    for key, val in qualities.items():
         total_cost = len(val) * prices[key]
         print('-' * 80)
         print(f'Quality: {key}' + ' '*50+ f'Price : {prices[key]}')
         print('=' * 80)
         for f in val:
            print(f)
         print('-' * 80)
         print(f'Total Number of {key} tomatos is {len(val)}  \t\t\t\t\t₹{total_cost}')
         print('-' * 80)
         print('\n')


files = [f for f in os.listdir('./images') if os.path.isfile(f'./images/{f}')]

for f in files:
    classify_quality(f'./images/{f}')

display()
