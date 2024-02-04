import cv2
import numpy as np
from typing import Tuple
from visionnest.image.colors import Colors


def draw_rectangle(
    image: np.ndarray, 
    top_left: Tuple, 
    bottom_right:Tuple, 
    color: Colors, 
    thickness: int=2,
    filled: bool=False
    ):
    """
    Draws a rectangle on an image using OpenCV.

    Parameters:
    ----------
    image : np.ndarray
        The image on which the rectangle will be drawn. This should be in the format of a NumPy array as read by cv2.imread.
    top_left : tuple
        The (x, y) coordinates of the top-left corner of the rectangle.
    bottom_right : tuple
        The (x, y) coordinates of the bottom-right corner of the rectangle.
    color : tuple
        The color of the rectangle. In BGR format (Blue, Green, Red), each value ranging from 0 to 255.
    thickness : int
        Thickness of the rectangle's edge. Pass -1 to fill the rectangle.
    filled: bool
        whether to fill the rectangle or not 

    Returns:
    -------
    np.ndarray
        The image with the rectangle drawn on it.
    """
    return cv2.rectangle(
        image, 
        top_left, 
        bottom_right, 
        color.as_bgr(), 
        thickness if not filled else -1
        )
        
