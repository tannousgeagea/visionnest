import os
import cv2
import logging
import numpy as np
from typing import Any, Iterator, List, Optional, Tuple, Union

def xyxy2xyxyn(xyxy:Union[List, Tuple], scale:Tuple) -> Tuple:
    """
    Convert bounding box coordinates from pixel format to normalized format.

    This function normalizes the bounding box coordinates based on the image dimensions. 
    The pixel coordinates (xmin, ymin, xmax, ymax) are converted to a normalized format 
    where each coordinate is represented as a fraction of the image's width or height.

    Parameters:
    - xyxy (tuple): A tuple of four integers (xmin, ymin, xmax, ymax) representing the bounding box coordinates in pixel format.
    - scale (tuple): A tuple of two integers (height, width) representing the dimensions of the image.

    Returns:
    - tuple: A tuple of four floats (xmin_n, ymin_n, xmax_n, ymax_n) representing the normalized bounding box coordinates.
    """
    return (
        xyxy[0] / scale[1], 
        xyxy[1] / scale[0],
        xyxy[2] / scale[1], 
        xyxy[3] / scale[0],
        )

def xyxyn2xyxy(xyxyn:Union[List, Tuple], scale:Tuple):
    """
    Convert bounding box coordinates from normalized format to pixel format.

    This function converts the normalized bounding box coordinates back to pixel format. 
    The normalized coordinates (xmin_n, ymin_n, xmax_n, ymax_n), represented as fractions 
    of the image's width or height, are scaled back to the pixel dimensions of the image.

    Parameters:
    - xyxyn (tuple): A tuple of four floats (xmin_n, ymin_n, xmax_n, ymax_n) representing the normalized bounding box coordinates.
    - scale (tuple): A tuple of two integers (height, width) representing the dimensions of the image.

    Returns:
    - tuple: A tuple of four integers (xmin, ymin, xmax, ymax) representing the bounding box coordinates in pixel format.
    """
    return (
        int(xyxyn[0] * scale[1]),
        int(xyxyn[1] * scale[0]),
        int(xyxyn[1] * scale[1]),
        int(xyxyn[2] * scale[0]),
    )

def xyxy2xywh(xyxy:Union[List, Tuple]):
    """
    Convert bounding box coordinates from (xmin, ymin, xmax, ymax) format to (x, y, width, height) format.

    Parameters:
    - xyxy (Tuple[int, int, int, int]): A tuple representing the bounding box coordinates in (xmin, ymin, xmax, ymax) format.

    Returns:
    - Tuple[int, int, int, int]: A tuple representing the bounding box in (x, y, width, height) format. 
                                 (x, y) are  the center of the bounding box.
    """
    w, h = xyxy[2] - xyxy[0], xyxy[3] - xyxy[1]
    return (
        xyxy[0] + w / 2,
        xyxy[1] + h / 2,
        w,
        h,
    )

def xywh2xyxy(xywh:Union[List, Tuple]):
    """
    Convert bounding box coordinates from (x, y, width, height) format to (xmin, ymin, xmax, ymax) format.

    This function assumes (x, y) as the center of the bounding box and calculates 
    the coordinates of the top-left corner (xmin, ymin) and the bottom-right corner (xmax, ymax).

    Parameters:
    - xywh (Tuple[float, float, float, float]): A tuple representing the bounding box in (x, y, width, height) format.

    Returns:
    - Tuple[float, float, float, float]: A tuple representing the bounding box in (xmin, ymin, xmax, ymax) format.
    """
    return (
        xywh[0] - xywh[2] / 2,
        xywh[1] - xywh[3] / 2,
        xywh[0] + xywh[2] / 2,
        xywh[1] + xywh[3] / 2,
    )

def poly2xyxy(poly:Union[List, Tuple]):
   """
    Convert a polygon representation to an axis-aligned bounding box.

    This function takes a list of vertices (x, y) of a polygon and calculates the minimum and 
    maximum x and y coordinates. The result is a bounding box (xmin, ymin, xmax, ymax) that 
    tightly encloses the polygon.

    Parameters:
    - poly (List[Tuple[int, int]]): A list of tuples, where each tuple represents a vertex (x, y) of the polygon.

    Returns:
    - Tuple[int, int, int, int]: A tuple representing the bounding box (xmin, ymin, xmax, ymax) of the polygon.
    """
    poly = np.array(poly)
    return (
        min(poly[..., 0]),
        min(poly[..., 1]),
        max(poly[..., 0]),
        max(poly[..., 1]),
    )

def xy2xyn(xy:Union[List, Tuple], scale:Tuple):
    """
    Convert actual polygon coordinates to normalized coordinates.

    This function scales actual pixel coordinates of a polygon to normalized coordinates
    in the range [0, 1], which are independent of the actual dimensions of the image or canvas.

    Parameters:
    - xy (list of tuples): List of actual coordinates in the format [(x1, y1), (x2, y2), ...].
    - scale (tuple): A tuple of two integers (height, width) representing the dimensions of the image.

    Returns:
    list of tuples: List of normalized coordinates in the format [(x1, y1), (x2, y2), ...].
    """
    return (
        (
            xy[i] / scale[1], 
            xy[i + 1] / scale[0]
        )
        for i in range(0, len(xy), 2)
    )

def xyn2xy(xyn:Union[List, Tuple], scale:Tuple):
    """
    Convert normalized polygon coordinates to actual coordinates.

    Normalized polygon coordinates are in the range [0, 1]. This function
    scales these coordinates to actual pixel coordinates based on the dimensions
    of the image or canvas.

    Parameters:
    - xyn (list of tuples): List of normalized coordinates in the format [(x1, y1), (x2, y2), ...].
    - image_shape (tuple): A tuple of two integers (height, width) representing the dimensions of the image.

    Returns:
    list of tuples: List of actual coordinates in the format [(x1, y1), (x2, y2), ...].
    """
    return (
        (
            int(xy[i] * scale[1]), 
            int(xy[i + 1] * scale[0])
        )
        for i in range(0, len(xy), 2)
    )

def xyxy_from_txtfile(txt_file:str):
    """
    Extract bounding box data from a text file.

    This function reads a text file containing bounding box data. Each line in the file should 
    represent a bounding box or a polygon, starting with a class ID followed by the vertices coordinates.
    If a line contains more than 4 coordinates, it is treated as a polygon and converted to an axis-aligned
    bounding box. The function returns class IDs and bounding boxes.

    Parameters:
    - txt_file (str): The path to the text file containing the bounding box data.

    Returns:
    - A tuple of two lists, the first being class IDs and 
      the second being bounding boxes (each box either as (xmin, ymin, xmax, ymax) or as a polygon)
    """
    boxes = []
    if not os.path.exists(txt_file):
        logging.warning("⚠️  Warning: %s not found !!!" %txt_file)
        return boxes

    with open(txt_file, 'r') as f:
        for label in f.readlines():
            class_id, x, y, w, h = [
                float(x) if float(x) != int(float(x)) else int(x)
                for x in label.replace("\n", "").split()
            ]
            boxes.append([class_id, x, y, w, h])
        
    return boxes

def xy_from_txtfile(txt_file:str):
    """
    Extract polygon data from a text file.

    This function reads a text file containing polygon data. Each line in the file should 
    represent a polygon, starting with a class ID followed by the vertices coordinates.
    The function returns class IDs and bounding boxes.

    Parameters:
    - txt_file (str): The path to the text file containing the bounding box data.

    Returns:
    - A tuple of two lists, the first being class IDs and 
      the second being polygon coordinate (each box either as (x, y) or as a polygon)
    """
    polygons = []
    if not os.path.exists(txt_file):
        logging.warning("⚠️  Warning: %s not found !!!" %txt_file)
        return polygons

    with open(txt_file, 'r') as f:
        for label in f.readlines():
            parts = label.replace("\n", "").split()
            class_id, vertices = int(parts[0]), parts[1:]
            xy = [(float(xy[i]), float(xy[i + 1])) for i in range(0, len(xy), 2)]
            polygons.append([class_id, xy])
        
    return polygons