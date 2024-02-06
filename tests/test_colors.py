import sys
sys.path.append('/home/appuser/src/visionnest')
from visionnest.image.colors import Colors


DEFAULT_COLOR_PALETTE = [
    "A351FB",
    "FF4040",
    "FFA1A0",
    "FF7633",
    "FFB633",
    "D1D435",
    "4CFB12",
    "94CF1A",
    "40DE8A",
    "1B9640",
    "00D6C1",
    "2E9CAA",
    "00C4FF",
    "364797",
    "6675FF",
    "0019EF",
    "863AFF",
    "530087",
    "CD3AFF",
    "FF97CA",
    "FF39C9",
]

LEGACY_COLOR_PALETTE = [
    "#A351FB",
    "#E6194B",
    "#3CB44B",
    "#FFE119",
    "#0082C8",
    "#F58231",
    "#911EB4",
    "#46F0F0",
    "#F032E6",
    "#D2F53C",
    "#FABEBE",
    "#008080",
    "#E6BEFF",
    "#AA6E28",
    "#FFFAC8",
    "#800000",
    "#AAFFC3",
]

def test_colors():

    for hex_code in LEGACY_COLOR_PALETTE:
        color = Colors.hex_to_rgb(hex_code)

        print("(%s, %s, %s)" %(color.r, color.g, color.b))


if __name__ == "__main__":
    test_colors()
