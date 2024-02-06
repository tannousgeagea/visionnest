import sys
sys.path.append('/home/appuser/src/visionnest')
from visionnest.image.colors import Colors
from visionnest.draw.rectangle import draw_rectangle
from visionnest.draw.label import put_text
from visionnest.annotators.boundingbox import BoxAnnotator

import numpy as np
import matplotlib.pyplot as plt


def test_box_label():
     # Create a blank black image
    img = np.zeros((300, 300, 3), dtype="uint8")

    # Coordinates of the rectangle's top-left and bottom-right corners
    top_left_corner = (10, 10)
    bottom_right_corner = (250, 250)

    # Color of the rectangle (Blue, Green, Red)
    rect_color = Colors(0, 255, 0)  # Green
    txt_color = Colors(0, 0, 0)
    # Thickness of the rectangle's edge
    rect_thickness = 3

    annotator = BoxAnnotator(im=img, line_width=2)

    xyxy = (50, 50, 250, 250)
    annotator.box_label(
        xyxy=xyxy,
        label="success",
        color=rect_color,
        txt_color=txt_color,
    )   

    plt.imshow(annotator.im)
    plt.show()

if __name__ == "__main__":
    test_box_label()