import sys
sys.path.append('/home/appuser/src/visionnest')
from visionnest.image.colors import Colors
from visionnest.draw.rectangle import draw_rectangle
from visionnest.draw.label import put_text

import numpy as np
import matplotlib.pyplot as plt

def test_put_text():
    # Create a blank black image
    img = np.zeros((300, 300, 3), dtype="uint8")

    # Coordinates of the rectangle's top-left and bottom-right corners
    top_left_corner = (10, 10)
    bottom_right_corner = (250, 250)

    # Color of the rectangle (Blue, Green, Red)
    rect_color = Colors(0, 255, 0)  # Green
    txt_color = Colors(255, 255, 255)
    # Thickness of the rectangle's edge
    rect_thickness = 3

    # Draw the rectangle
    img_with_rect = draw_rectangle(img, top_left_corner, bottom_right_corner, rect_color, rect_thickness)
    img_with_text = put_text(img_with_rect, top_left_corner, "Success", color=txt_color, line_width=2)

    # Display the image
    plt.imshow(img_with_rect)
    plt.show()

    plt.imshow(img_with_text)
    plt.show()

if __name__ == "__main__":
    test_put_text()