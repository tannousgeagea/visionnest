import random
import logging
from typing import Union
from typing import List, Tuple
from .colors import Colors

class ColorPalette:
    """
    A class to manage and retrieve colors, including predefined color palettes.

    This class allows adding individual colors or entire color palettes to a collection, 
    retrieving colors by name, and obtaining a random color from the palette.
    Colors are stored and handled as RGB tuples.

    Attributes:
        colors (dict): A dictionary to store colors with their names as keys.

    Methods:
        add_color(name, rgb): Adds a color to the palette.
        add_palette(name, palette): Adds a set of colors to the palette under a palette name.
        get_color(name): Retrieves a color by its name.
        random_color(): Returns a random color from the palette.
    """

    def __init__(self,):
        """
        Initializes the ColorPalette instance with an empty colors dictionary.
        """
        self.colors = []
        self._init_standard_palettes()

    def _init_standard_palettes(self):
        """
        Initializes standard color palettes.
        """
        # Add more palettes as needed
        basic_palette = [
            (255, 0, 0), (0, 255, 0), (0, 0, 255),
            (255, 255, 0), (0, 255, 255), (255, 0, 255),
            (128, 128, 128), (163, 81, 251), (255, 64, 64),
            (255, 161, 160), (255, 118, 51), (255, 182, 51),
            (209, 212, 53), (76, 251, 18), (148, 207, 26),
            (64, 222, 138), (27, 150, 64), (0, 214, 193),
            (46, 156, 170), (0, 196, 255), (54, 71, 151),
            (102, 117, 255), (0, 25, 239), (134, 58, 255),
            (83, 0, 135), (205, 58, 255), (255, 151, 202),
            (255, 57, 201), (255, 0, 0), (230, 25, 75),
            (60, 180, 75), (255, 225, 25), (0, 130, 200),
            (245, 130, 49), (145, 30, 180), (70, 240, 240),
            (240, 50, 230), (210, 245, 60), (250, 190, 190),
            (0, 128, 128), (230, 190, 255), (170, 110, 40),
            (255, 250, 200), (128, 0, 0), (170, 255, 195),
        ]
        self.add_palette(basic_palette)

    def add_color(self, color_code: Union[tuple, list, Colors]):
        """
        Adds a new color to the palette.
        """
        if isinstance(color_code, Tuple):
            r, g, b =  color_code
            self.colors.append(Colors(r, g, b))
        elif isinstance(color_code, str):
            self.colors.append(Colors.hex_to_rgb(color_code))
        elif isinstance(color_code, Colors):
            self.colors.append(color_code)
        else:
            logging.warning("⚠️  Unsupported color code: {}".format(color_code))

    def add_palette(self, palette: list):
        """
        Adds a set of named colors to the palette.
        
        Parameters:
            palette_name (str): A name for the palette for reference.
            palette (dict): A dictionary of color names and their RGB values.
        """
        for rgb in palette:
            self.add_color(rgb)

    def override_color(self, colors: List):
        """
        override a set of named colors to the palette.
        
        Parameters:
            palette_name (str): A name for the palette for reference.
        """
        lookup_colors = []
        for color_code in colors:
            if isinstance(color_code, Tuple):
                r, g, b =  color_code
                lookup_colors.append(Colors(r, g, b))
            elif isinstance(color_code, str):
                lookup_colors.append(Colors.hex_to_rgb(color_code))
            elif isinstance(color_code, Colors):
                lookup_colors.append(color_code)
            else:
                logging.warning("⚠️  Unsupported color code: {}".format(color_code))
        if len(lookup_colors):
            self.colors = lookup_colors + self.colors

    def get_color_by_index(self, index: int):
        """
        Retrieves a color by its index in the palette.
        """
        if index < 0 or index >= len(self.colors):
            raise IndexError("Color index out of range")
        return self.colors[index]

    def random_color(self):
        """
        Returns a random color from the palette.
        """
        return random.choice(self.colors) if self.colors else None
