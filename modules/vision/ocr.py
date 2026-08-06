"""
OCR
Project PEGASUS
"""

import pytesseract
from PIL import Image


class OCR:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def read(self, source):

        # If a file path is given
        if isinstance(source, str):

            image = Image.open(source)

        # If a PIL Image is given
        else:

            image = source

        text = pytesseract.image_to_string(image)

        return text.strip()