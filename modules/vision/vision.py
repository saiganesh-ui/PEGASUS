"""
Vision
Project PEGASUS
"""

from modules.vision.image_loader import ImageLoader
from modules.vision.image_analyzer import ImageAnalyzer
from modules.vision.screenshot import Screenshot


class Vision:

    def __init__(self):

        self.loader = ImageLoader()
        self.analyzer = ImageAnalyzer()
        self.screenshot = Screenshot()

    def analyze(self, path):

        image = self.loader.load(path)

        return self.analyzer.analyze(image)

    def analyze_screen(self):

        path = self.screenshot.capture()

        return self.analyze(path)