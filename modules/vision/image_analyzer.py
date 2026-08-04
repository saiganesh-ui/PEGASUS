"""
Image Analyzer
Project PEGASUS
"""

from modules.vision.image_result import ImageResult


class ImageAnalyzer:

    def analyze(self, image):

        result = ImageResult()

        result.width = image.width
        result.height = image.height
        result.mode = image.mode
        result.format = image.format

        return result