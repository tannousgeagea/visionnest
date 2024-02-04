"""
-------------------------------------------------------------------
core of image
File: core.py

Description: this module contain information about the image

Author: Tannous Geagea
Maintainer: Tannous Geagea
Created: February 4th, 2024
Copyright: © [2024] by Tannous Geagea
License: MIT
-------------------------------------------------------------------
"""

import cv2

class Image:
    """
    A class to represent an image and its different formats.

    Attributes:
        _data: The raw data of the image.
    """
    def __init__(self, data):
        """
        Constructs all the necessary attributes for the image object.

        Parameters:
            data: The raw data of the image.
        """
        self._data = data

    @property
    def data(self):
        """
        Returns the raw image data.

        Returns:
            The raw image data as a NumPy array.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the image data.

        Parameters:
            value: The new image data to set.
        """
        self._data = value

    @property
    def shape(self):
        return self.data.shape
    
    @property
    def rgb(self):
        """
        Returns the image in RGB format.

        Returns:
            The image converted to RGB format.
        """
        return self.convert_to_rgb()

    @property
    def bgr(self):
        """
        Returns the image in BGR format.

        Returns:
            The image converted to BGR format.
        """
        return self.convert_to_bgr()

    def convert_to_rgb(self):
        """
        Converts the image to RGB format.

        This is a placeholder method and should be replaced with actual image processing logic.

        Returns:
            The image in RGB format.
        """
        # Placeholder for actual conversion logic
        return cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)

    def convert_to_bgr(self):
        """
        Converts the image to BGR format.

        This is a placeholder method and should be replaced with actual image processing logic.

        Returns:
            The image in BGR format.
        """
        # Placeholder for actual conversion logic
        return cv2.cvtColor(self.data, cv2.COLOR_RGB2BGR)
    