import cv2
import numpy as np
from typing import Tuple, Optional
from visionnest.image.colors import Colors
from .rectangle import draw_rectangle
def put_text(
    image:np.ndarray,
    p1: Tuple,
    label:str="",
    color: Colors=Colors(0, 0, 0),
    line_width:int=3,
    lineType=cv2.LINE_AA,
    background_color: Optional[Colors]=None,

    ):
    tf = max(line_width - 1, 1)  # font thickness
    w, h = cv2.getTextSize(label, 0, fontScale=line_width / 3, thickness=tf)[0]  # text width, height
    outside = p1[1] - h >= 3
    p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3

    if not background_color is None:
        draw_rectangle(image, p1, p2, background_color, filled=True)

    return cv2.putText(
        image,
        label, 
        (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
        0,
        line_width / 3,
        color.as_bgr(),
        thickness=tf,
        lineType=cv2.LINE_AA)

