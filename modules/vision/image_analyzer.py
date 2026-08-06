"""
Image Analyzer
Project PEGASUS
"""

from modules.vision.image_result import ImageResult
from modules.vision.ocr import OCR
from modules.vision.screen_analyzer import ScreenAnalyzer
from modules.vision.reasoning_engine import ReasoningEngine
from modules.vision.decision_engine import DecisionEngine


class ImageAnalyzer:

    def __init__(self):

        self.ocr = OCR()
        self.screen = ScreenAnalyzer()
        self.reasoner = ReasoningEngine()
        self.decision = DecisionEngine()

    def analyze(self, image):

        result = ImageResult()

        # Image Information
        result.width = image.width
        result.height = image.height
        result.mode = image.mode
        result.format = image.format

        # OCR
        text = self.ocr.read(image)
        result.text = text

        # Screen Analysis
        screen = self.screen.analyze(text)

        result.application = screen.application
        result.file = screen.file
        result.language = screen.language
        result.line = screen.line
        result.error = screen.error
        result.summary = screen.summary
        result.screen_type = screen.screen_type

        # Reasoning
        result.reasoning = self.reasoner.think(result)

        # Decision
        result.decision = self.decision.decide(result)

        return result