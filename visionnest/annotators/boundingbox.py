"""
-------------------------------------------------------------------
box annotators
File: boundingbox.py

Description: this module contain information about the image

Author: Tannous Geagea
Maintainer: Tannous Geagea
Created: February 4th, 2024
Copyright: © [2024] by Tannous Geagea
License: MIT
-------------------------------------------------------------------
"""

import cv2
import cv2
import sys
import logging
import numpy as np
from typing import Any
from typing import List
from typing import Tuple
from typing import Union
from typing import Optional

from visionnest.draw.label import put_text
from visionnest.image.colors import Colors
from visionnest.detection.core import Detections
from visionnest.draw.rectangle import draw_rectangle
from visionnest.image.color_palette import ColorPalette

class BoxAnnotator:
    """
    This class provides functionality for drawing bounding boxes on images. 
    It is primarily used for visualizing object detection results or for annotating ground truth data in images.

    The class takes an image in the form of a numpy array and allows users to specify the line width and font size 
    for the annotations. The bounding boxes can be drawn around detected objects in the image, providing a visual tool 
    for analyzing detection results or for marking objects in an image dataset.

    Attributes:
        im (np.ndarray): The image on which annotations will be drawn, represented as a numpy array.
        im_shape (tuple): The shape (dimensions) of the input image.
        line_width (int): The thickness of the bounding box lines. Defaults to 2.
        font_size (int): The font size used for labeling the boxes. If None, a default size is chosen based on the image size.
        lw (int): Calculated line width for drawing, with a minimum value of 2. If line_width is specified, lw is set to that value.

    Example:
        >>> image = np.array(Image.open('example.jpg'))
        >>> annotator = BoxAnnotator(image, line_width=3, font_size=12)
        # Now you can use methods of the BoxAnnotator class to draw bounding boxes on 'image'.
    """

    def __init__(self, im: np.ndarray, line_width:int=2, font_size:int=None):
        self.im = im
        self.im_shape = self.im.shape
        self.line_width = line_width
        self.font_size = font_size
        self.lw = line_width or max(round(sum(im.shape) / 2 * 0.003), 2)  # line width
    

    def box_label(
        self,
        xyxy:Union[List, Tuple],
        label:str="",
        color: Union[Colors, Tuple, str]=None,
        txt_color:Tuple=None,
    ):
        """
        Draws a bounding box on the image with an optional label.

        This method takes coordinates for the bounding box and draws it on the image. 
        It can also label the box with a specified text. The method supports customization of the box and text color. 
        If a string is provided for the box color, it is converted from a hex color code to RGB.

        Parameters:
            xyxy (Union[List, Tuple]): Coordinates for the bounding box in the format (x1, y1, x2, y2), where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner.
            label (str, optional): The text label to be placed near the bounding box. Defaults to an empty string, meaning no label.
            color (Union[Tuple, str], optional): The color of the bounding box. Can be a tuple of RGB values or a hex color code as a string. If None, a default color is chosen.
            txt_color (Tuple, optional): The color of the text label, given as a tuple of RGB values. If None, a default color is chosen.

        Example:
            >>> annotator = BoxAnnotator(image)
            >>> annotator.box_label(xyxy=[50, 100, 150, 200], label='Object', color='ff0000', txt_color=(255, 255, 255))
            # This will draw a red box from (50, 100) to (150, 200) with a white 'Object' label.
        """

        if isinstance(color, str):
            color = Colors.hex_to_rgb(color)
        elif isinstance(color, Tuple):
            r, g, b = color
            color = Colors(r, g, b)
        
        p1, p2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
        draw_rectangle(self.im, p1, p2, color, thickness=self.lw, filled=False)
        if label:
            put_text(
                self.im,
                label=label,
                p1=p1,
                color=txt_color,
                line_width=self.lw,
                background_color=color,
            )

    def annotate(
        self,
        detections: Detections,
        labels:Optional[List]=None,
        colors: Union[np.ndarray, Tuple]=None,
        txt_color: Union[Tuple, str, Colors]=None,
        ):
        """
        Annotates the image with bounding boxes based on the provided detections.

        This method draws bounding boxes around detected objects in the image. It optionally accepts custom labels and colors for the boxes. If the number of provided colors is less than the number of detections, a warning is logged. Each detection is represented by a bounding box, which is drawn using the `box_label` method.

        Parameters:
            detections (Detections): An object containing detection data, including bounding box coordinates and class IDs.
            labels (Optional[List], optional): A list of labels corresponding to each detection. Defaults to None, in which case no labels are used.
            colors (Union[np.ndarray, Tuple], optional): An array or a tuple of colors to be used for each detection's bounding box. Defaults to None, in which case a default color palette is used.
            txt_color (Union[Tuple, str, Colors], optional): The color to be used for the text of the labels. Can be specified as a tuple, a string, or a `Colors` object. Defaults to None.

        Raises:
            Exception: Logs an error if an unexpected error occurs during the annotation process.

        Example:
            >>> annotator = BoxAnnotator(image)
            >>> detections = Detections(...)  # Detections object with bounding box and class information
            >>> annotator.annotate(detections, labels=["label1", "label2"], colors=[(255,0,0), (0,255,0)])
            # This will annotate the image with the specified detections, labels, and colors.
        """

        color_palette = ColorPalette()
        if not colors is None:
            if len(colors) < len(detections):
                logging.warning(
                    f"⚠️  colors provided by users of length {len(colors)} "
                    f"is out of bounds for detections of length {len(detections)}"
                )
        
            color_palette.add_color(colors)
        
        try:
            for i, xyxy in enumerate(detections.xyxy):
                xyxy = xyxy.astype(int)
                color_idx = detections.class_id[i] if not detections.class_id is None else i 
                self.box_label(
                    xyxy=xyxy,
                    label=labels[i] if not labels is None else "",
                    color=color_palette.get_color_by_index(color_idx),
                    txt_color=txt_color,
                )

        except Exception as err:
            logging.error("Unexpected Error in annotate: %s" % err)



