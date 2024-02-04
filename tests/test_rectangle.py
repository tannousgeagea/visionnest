# Example usage
import sys
sys.path.append('/home/appuser/src/visionnest')
from visionnest.image.colors import Colors
from visionnest.draw.rectangle import draw_rectangle

import numpy as np
import matplotlib.pyplot as plt


def test_draw_rectangle():
    # Create a blank black image
    img = np.zeros((300, 300, 3), dtype="uint8")

    # Coordinates of the rectangle's top-left and bottom-right corners
    top_left_corner = (50, 50)
    bottom_right_corner = (250, 250)

    # Color of the rectangle (Blue, Green, Red)
    rect_color = Colors(0, 255, 0)  # Green

    # Thickness of the rectangle's edge
    rect_thickness = 3

    # Draw the rectangle
    img_with_rect = draw_rectangle(img, top_left_corner, bottom_right_corner, rect_color, rect_thickness)

    # Display the image
    plt.imshow(img_with_rect)
    plt.show()


def test_draw_rectangle_filled():
    # Create a blank black image
    img = np.zeros((300, 300, 3), dtype="uint8")

    # Coordinates of the rectangle's top-left and bottom-right corners
    top_left_corner = (50, 50)
    bottom_right_corner = (250, 250)

    # Color of the rectangle (Blue, Green, Red)
    rect_color = Colors(0, 255, 0)  # Green

    # Thickness of the rectangle's edge
    rect_thickness = 3

    # Draw the rectangle
    img_with_rect = draw_rectangle(img, top_left_corner, bottom_right_corner, rect_color, rect_thickness, filled=True)

    # Display the image
    plt.imshow(img_with_rect)
    plt.show()


if __name__ == "__main__":

    test_draw_rectangle()
    test_draw_rectangle_filled()