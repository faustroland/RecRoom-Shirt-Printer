"""
Converts a PNG image into strings of predefined length
How is it encoded:
    the number in front of a char represents how many pixels of the same color are in a row,
    chars !#$%&()*+,./:;<=>?@[Ñ]^_{|}~¢£¤¥¦§¨©ª«¬Ö®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÈÌÐ represent the color.
    There's 62 colors including eraser and tan, eraser is not recommended as it leaves an edge
"""
import os
import subprocess
import sys
import time
import tkinter
from math import sqrt
from pathlib import Path
from tkinter import filedialog
from typing import Tuple, List

try:
    import pyautogui
    import pyperclip
    from PIL import Image, ImageGrab
except ModuleNotFoundError:
    print(f'Please execute the following line and run the script again:\n'
          f'{sys.executable} -m pip install -U PyAutoGUI pyperclip Pillow')
    # Ask the user to install all the necessary packages automatically
    if input("Proceed to run the command automatically? [yes/no] ").find("yes") != -1:
        subprocess.call(f"{sys.executable} -m pip install -U PyAutoGUI pyperclip Pillow")
    exit()

MaxStringLength: int = 280  # Maximum length string

# Typing alias for color
PixelColor = Tuple[int, int, int]

# All of RecRoom color in order + tan marker + eraser
RR_PALETTE: dict = {
(255, 255, 255): "!",
(150, 113, 116): "#",
(211, 185, 188): "$",
(184, 152, 155): "%",
(231, 217, 226): "&",
(188, 117, 125): "(",
(166, 134, 138): ")",
(252, 233, 235): "*",
(197, 166, 170): "+",
(228, 205, 208): ",",
(166, 122, 123): ".",
(183, 137, 144): "/",
(243, 247, 246): ":",
(219, 196, 199): ";",
(173, 111, 115): "<",
(237, 231, 233): "=",
(202, 175, 179): ">",
(176, 127, 133): "?",
(255, 242, 245): "@",
(243, 221, 224): "[",
(153, 121, 125): "Ñ",
(188, 160, 164): "]",
(237, 214, 216): "^",
(175, 145, 148): "_",
(160, 128, 130): "{",
(179, 121, 122): "|",
(241, 238, 239): "}",
(160, 113, 117): "~",
(224, 216, 219): "¢",
(185, 128, 135): "£",
(246, 255, 254): "¤",
(184, 113, 118): "¥",
(174, 135, 140): "¦",
(231, 225, 228): "§",
(248, 228, 230): "¨",
(250, 250, 249): "©",
(185, 121, 131): "ª",
(173, 117, 124): "«",
(169, 128, 132): "¬",
(172, 118, 117): "Ö",
(255, 248, 254): "®",
(247, 242, 243): "¯",
(167, 115, 121): "°",
(226, 221, 223): "±",
(173, 122, 130): "²",
(160, 120, 124): "³",
(242, 253, 250): "´",
(178, 115, 122): "µ",
(254, 238, 241): "¶",
(179, 115, 116): "·",
(183, 118, 120): "¸",
(178, 122, 128): "¹",
(254, 254, 250): "º",
(173, 123, 125): "»",
(255, 247, 246): "¼",
(184, 120, 125): "½",
(166, 122, 128): "¾",
(183, 115, 124): "¿",
(251, 250, 254): "À",
(250, 246, 247): "È",
(250, 254, 252): "ß",
(178, 118, 119): "Ä",
(255, 250, 250): "ê",
(255, 246, 250): "ö",
(180, 119, 125): "Ø",
(247, 249, 250): "Ð",
(176, 116, 116): "Ý",
(249, 254, 255): "ä",
(253, 254, 253): "î",
(255, 252, 255): "Œ",
(252, 255, 255): "Ç",
(179, 114, 118): "Ž",
(255, 251, 252): "ÿ",
(253, 253, 255): "Ú",
(176, 116, 118): "É",
(177, 115, 115): "Ê",
(252, 253, 252): "Æ",
(255, 254, 254): "Ë",
(255, 254, 255): "Ù",
(176, 116, 116): "Ü",
}

# All the RecRoom colors in one list. [R, G, B, R, G, B,...]
ALL_COLORS = [num for tup in RR_PALETTE.keys() for num in tup]


def get_image(check_palette: bool = True) -> Image:
    """
    Open file explorer, wait for user to open a PNG image
    :return: The image
    """
    print("Open image", end="\r")
    root = tkinter.Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename(filetypes=[("Image", "*.png")])
    root.destroy()

    img = None
    if img_path:
        img = Image.open(img_path)

    if check_palette:
        # If the image has attributed `palette` its metadata is a bit different.
        # To solve this just open the image in paint and save it
        if img.palette:
            print("Image has `Palette` attribute. Open it in Paint and save.")
            os.system(f'mspaint.exe "{Path(img_path)}"')
            return None

    return img


def closest_color(pixel_color: PixelColor) -> PixelColor:
    """
    Take an RGB value and find the closest color in `RR_PALETTE`

    It is recommended you use external programs to convert and dither images.
    2 ACO (swatch) files are included if you're using Photoshop

    :param pixel_color: The color of the pixel of the image
    :return: The color from `RR_PALETTE` that is closest to `pixel_color`
    """
    r, g, b = pixel_color
    color_diffs: List[tuple[float, PixelColor]] = []
    for key in RR_PALETTE:
        cr, cg, cb = key
        color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, key))
    return min(color_diffs)[1]


def progress_update(y: int, img: Image, prefix='Progress', suffix='', length=50) -> None:
    """
    Display a progress bar in the console
    :param y: The `y` value of the image
    :param img: The image
    :param prefix: Optional: Text in-front of the progress bar
    :param suffix: Optional: Text behind the progress bar
    :param length: Optional: The length of the progress bar
    """
    completed = int(length * y // img.height)
    empty = length - completed
    bar = "#" * completed + " " * empty
    percent = f"{100 * (y / float(img.height)):.2f}"
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="\r")

    # Print New Line on Complete
    if y == img.height:
        print(" " * (length + 30), end="\r")


def quantize(img, ask_for_dither: bool = True, dither: int = 0, open_image: bool = True) -> Image:
    img = img.convert("RGB")

    if ask_for_dither:
        dither = 0 if "n" in input("Dither the image? [y/n] ").lower() else 1

    palette_image = Image.new("P", img.size)
    palette_image.putpalette(ALL_COLORS)
    new_image = img.quantize(palette=palette_image,
                             dither=dither).convert("RGB")

    if open_image:
        print("Opening the final image...")
        new_image.show()

    return new_image


def encode(img: Image, vertical_print: bool = False, dither_: bool = True) -> list[str] or None:
    """
    Take an image and encode it into a list of {`MaxStringLength`}-char strings.
    ...[number of pixels][color]...

    :param img: The image to be encoded.
    :param vertical_print: Encode the image vertically (for Ashers printer)
    :param dither_: Should the image be dithered
    :return: List of {`MaxStringLength`} char long strings
    """
    pixel_color: List[str] = []
    full_image = Image.new("RGB", img.size)
    dither = False

    # Just so pycharm doesn't complain
    x, y = 0, 0

    if dither_:
        img = quantize(img)

    # `vertical_print` just changes the orientation of the encoding process.
    for y in range(img.height):
        for x in range(img.width):
            p = img.getpixel((y, x) if vertical_print else (x, y))  # Gets the color of the pixel at `x, y`
            if len(p) == 4:  # If the value is RGBA, the last `int` is removed
                p = p[:3]
            try:
                # Check if the image has already been dithered, else find the closest color
                p = RR_PALETTE[p]
            except KeyError:
                dither = True
                p = closest_color(p)
                full_image.putpixel((y, x) if vertical_print else (x, y), p)
                p = RR_PALETTE[p]
                # closest_color(p)
            pixel_color.append(p)
        # Print the progress
        progress_update(y + 1, img, "Encoding")

    if dither and dither_:
        full_image.show()

    colors: List[Tuple[int, str]] = []
    count: int = 0
    current_color: str = pixel_color[0]
    # `count` is the amount of `current_color` in a row

    for c in pixel_color:
        if c != current_color:
            colors.append((count, current_color))
            count = 0
            current_color = c
        count += 1
    colors.append((count, current_color))

    print(f"Compressed {len(pixel_color)} chars into {len(colors)} chars")
#    offset=1024*1024
#    s: str = str(offset)+"X"
    s: str = ""
    img_data: List[str] = []
    for amount, color in colors:
        if amount > 1:
            ns = f"{amount}{color}"
        else:
            ns = color

        if len(s + ns) > MaxStringLength:  # 512
            img_data.append(s)
            s = ""
        s += ns

    img_data.append(s)
    return img_data


def main(list_size: int, output_strings: bool = False, wait_for_input: bool = False):
    """
    Function to tie together all others.
    Prompt for image, encode and output

    :param list_size: The max list size; 50 for `Variable` importing, 64 for `List Create` importing
    :param output_strings: Print the encoded image strings into the console
    :param wait_for_input: Wait for the user to continue. Useful when running this file directly so that it stays open
    """

    img: Image = get_image()
    if not img:
        exit()

    img_data: list[str] = encode(img)

    with open("image_data.txt", "w") as strings_file:
        strings_file.writelines("\n".join(img_data))

    if output_strings:
        print("Copying strings\n_______________\n")
        time.sleep(2)
        # Print all image data strings
        print("\n\n".join(img_data))

    # Print amount of {`MaxStringLength`} char long strings, image dimensions and total `List Create`s needed.
    print(f"\nGenerated {len(img_data) + 2} strings for image WxH {img.width}x{img.height}")
    print(f"Space needed: {len(img_data) // list_size} Lists (+ {len(img_data) % list_size})")

    if wait_for_input:
        input("Press enter to continue")

    return img, img_data


if __name__ == '__main__':
    try:
        main(output_strings=True,
             wait_for_input=True,
             list_size=50 if "1" in input("1. Variable Import\n2. List Create Import\n> ") else 64)
    except KeyboardInterrupt:
        pass
