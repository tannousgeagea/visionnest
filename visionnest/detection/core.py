"""
-------------------------------------------------------------------
core of detections
File: core.py

Description: this module contain information about the detections

Author: Tannous Geagea
Maintainer: Tannous Geagea
Created: February 4th, 2024
Copyright: © [2024] by Tannous Geagea
License: MIT
-------------------------------------------------------------------
"""

import numpy as np
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Iterator 
from typing import Optional
from dataclasses import dataclass


@dataclass
class Detections:
    """
    Data class containing information about the detections.
    Attributes:
        image: a numpy array of shape (H, W, C), where H and W correspond to
            the height and width of the image respectively. C is the number of
            color channels. The image is required to be in RGB format since that
            is a requirement of the Matplotlib library. The image is also expected
            to be in the range [0, 255]
        xyxy (array): An array of shape `(n, 4)` containing
            the bounding boxes coordinates in format `[x1, y1, x2, y2]`
        poly: (List[Tuple[int, int]]): A list of tuples, where each tuple represents a vertex (x, y) of the polygon.
            `(n, H, W)` containing the segmentation masks.
        confidence (Optional[np.ndarray]): An array of shape
            `(n,)` containing the confidence scores of the detections.
        class_id (Optional[np.ndarray]): An array of shape
            `(n,)` containing the class ids of the detections.
        tracker_id (Optional[np.ndarray]): An array of shape
            `(n,)` containing the tracker ids of the detections.
        object_length (Optional[np.ndarray]): An array of shape
            `(n,)` containing the object_length of the detections.
        object_area (Optional[np.ndarray]): An array of shape
            `(n,)` containing the object area of the detections.
    """

    xyxy: np.ndarray
    poly: Optional[np.ndarray]=None
    confidence: Optional[np.ndarray]=None
    class_id: Optional[np.ndarray]=None
    tracker_id: Optional[np.ndarray]=None
    object_length: Optional[np.ndarray]=None
    object_area: Optional[np.ndarray]=None

    def __len__(self):
        """
        Returns the number of detections in the Detections object.
        """
        return len(self.xyxy)

    def __getitem__(self, index):
        """
        Get a subset of the Detections object.

        Args:
            index (Union[int, slice, List[int], np.ndarray]):
                The index or indices of the subset of the Detections

        Returns:
            (Detections): A subset of the Detections object.
        """
        if isinstance(index, int):
            index = [index]
        return Detections(
            xyxy=self.xyxy[index],
            poly=self.poly[index] if self.poly is not None else None,
            confidence=self.confidence[index] if self.confidence is not None else None,
            class_id=self.class_id[index] if self.class_id is not None else None,
            tracker_id=self.tracker_id[index] if self.tracker_id is not None else None,
            object_length=self.object_length[index] if self.object_length is not None else None,
            object_area=self.object_area[index] if self.object_area is not None else None,
        )


    def __iter__(
        self,
    ) -> Iterator[
        Tuple[
            np.ndarray,
            Optional[np.ndarray],
            Optional[np.ndarray],
            Optional[np.ndarray],
            Optional[np.ndarray],
            Optional[np.ndarray],
            Optional[np.ndarray]
        ]
    ]:
        """
        Iterates over the Detections object and yield a tuple of
        `(xyxy, poly, confidence, class_id, tracker_id, object_length, object_area)` for each detection.
        """
        for i in range(len(self.xyxy)):
            yield (
                self.xyxy[i],
                self.poly[i] if self.poly is not None else None,
                self.confidence[i] if self.confidence is not None else None,
                self.class_id[i] if self.class_id is not None else None,
                self.tracker_id[i] if self.tracker_id is not None else None,
                self.object_length[i] if self.object_length is not None else None,
                self.object_area[i] if self.object_area is not None else None,
            )


    def __eq__(self, other):
        return all(
            [
                np.array_equal(self.xyxy, other.xyxy),
                any(
                    [
                        len(self.poly) and len(self.other.poly),
                        np.array_equal(self.poly, other.poly),
                    ]
                ),
                any(
                    [
                        len(self.class_id) and (other.class_id),
                        np.array_equal(self.class_id, other.class_id),
                    ]
                ),
                any(
                    [
                        (self.confidence)and (other.confidence),
                        np.array_equal(self.confidence, other.confidence),
                    ]
                ),
                any(
                    [
                        (self.tracker_id) and (other.tracker_id ),
                        np.array_equal(self.tracker_id, other.tracker_id),
                    ]
                ),
            ]
        )