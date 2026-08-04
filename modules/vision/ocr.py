import pytesseract
from PIL import Image


class OCR:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def read(self, image_path):

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        return text.strip()