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

from typing import Tuple
from dataclasses import dataclass

@dataclass
class Colors:
    """
    Represents a color in RGB format.

    This class provides methods to work with colors, including creating colors from hex
    codes, converting colors to hex strings, RGB tuples, and BGR tuples.

    Attributes:
        r (int): Red channel value (0-255).
        g (int): Green channel value (0-255).
        b (int): Blue channel value (0-255).

        ```

    | Constant   | Hex Code   | RGB              |
    |------------|------------|------------------|
    | `WHITE`    | `#FFFFFF`  | `(255, 255, 255)`|
    | `BLACK`    | `#000000`  | `(0, 0, 0)`      |
    | `RED`      | `#FF0000`  | `(255, 0, 0)`    |
    | `GREEN`    | `#00FF00`  | `(0, 255, 0)`    |
    | `BLUE`     | `#0000FF`  | `(0, 0, 255)`    |
    | `YELLOW`   | `#FFFF00`  | `(255, 255, 0)`  |
    | `ROBOFLOW` | `#A351FB`  | `(163, 81, 251)` |
    """

    r: int
    g: int
    b: int

    @classmethod
    def hex_to_rgb(cls, hex_code: str):
        """
        Converts a hexadecimal color code to an RGB tuple.

        Parameters:
        ----------
        hex_code : str
            Hexadecimal string representing a color.

        Returns:
        -------
        tuple
            A tuple representing the RGB values.

        Raises:
        ------
        ValueError: If hex_code is not 6 characters long.
        """
        hex_code = hex_code.lstrip('#')
        if len(hex_code) != 6:
            raise ValueError("Hex code must be 6 characters long")
        r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        return cls(r, g, b)

    @staticmethod
    def rgb_to_hex() -> str:
        """
        Converts an RGB tuple to a hexadecimal string.

        Parameters:
        ----------
        rgb_tuple : tuple
            A tuple representing the RGB values.

        Returns:
        -------
        str
            Hexadecimal string representing the color.
        """
        return '#{0:02x}{1:02x}{2:02x}'.format(self.r, self.g, self.b)

    def to_hex(self):
        """
        Returns the hexadecimal string of the color.

        Returns:
        -------
        str
            Hexadecimal string representing the color.
        """
        return self.rgb_to_hex(self.rgb)

    def as_rgb(self) -> Tuple[int, int, int]:
        """
        Returns the color as an RGB tuple.

        Returns:
            Tuple[int, int, int]: RGB tuple.
            ```
        """
        return self.r, self.g, self.b

    def as_bgr(self) -> Tuple[int, int, int]:
        """
        Returns the color as a BGR tuple.

        Returns:
            Tuple[int, int, int]: BGR tuple.

        Example:
            ```python
            import supervision as sv

            sv.Color(r=255, g=255, b=0).as_bgr()
            # (0, 255, 255)
            ```
        """
        return self.b, self.g, self.r

    @classmethod
    def WHITE(cls):
        return cls.hex_to_rgb("#FFFFFF")

    @classmethod
    def BLACK(cls):
        return cls.hex_to_rgb("#000000")

    @classmethod
    def RED(cls):
        return cls.hex_to_rgb("#FF0000")

    @classmethod
    def GREEN(cls):
        return cls.hex_to_rgb("#00FF00")

    @classmethod
    def BLUE(cls):
        return cls.hex_to_rgb("#0000FF")

    @classmethod
    def YELLOW(cls):
        return cls.hex_to_rgb("#FFFF00")

    @classmethod
    def ROBOFLOW(cls):
        return cls.hex_to_rgb("#A351FB")