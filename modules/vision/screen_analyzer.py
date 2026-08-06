"""
Screen Analyzer
Project PEGASUS
Author: Sai Ganesh
"""

from modules.vision.image_result import ImageResult
from modules.vision.app_detector import AppDetector
from modules.vision.error_detector import ErrorDetector
from modules.vision.file_detector import FileDetector
from modules.vision.line_detector import LineDetector
from modules.vision.language_detector import LanguageDetector
from modules.vision.reasoning_engine import ReasoningEngine
from modules.vision.decision_engine import DecisionEngine


class ScreenAnalyzer:

    def __init__(self):

        self.app_detector = AppDetector()
        self.error_detector = ErrorDetector()
        self.file_detector = FileDetector()
        self.line_detector = LineDetector()
        self.language_detector = LanguageDetector()
        self.reasoner = ReasoningEngine() 
        self.decision_engine = DecisionEngine()

    def analyze(self, text):

        result = ImageResult()

        # Detect application
        result.application = self.app_detector.detect(text)

        # Detect errors
        result.error = self.error_detector.detect(text)

         # Detect current file
        result.file = self.file_detector.detect(text)
        
        # Detect Language 
        result.language = self.language_detector.detect(result.file)
        
        # Detect current line
        result.line = self.line_detector.detect(text)

        # Screen Type

        if result.application:

            app = result.application["name"]

            if app == "Visual Studio Code":

                result.screen_type = "code_editor"

            elif "Chrome" in app:

                result.screen_type = "browser"

            elif app == "File Explorer":

                result.screen_type = "file_manager"

            else:

                result.screen_type = "application"

        # Summary

            parts = []

            if result.application:

                parts.append(
                    f"Application: {result.application['name']}"
                )

            if result.file:

                parts.append(
                    f"File: {result.file['name']}"
                )

            if result.language:

                parts.append(
                    f"Language: {result.language['name']}"
                )

            if result.line:

                parts.append(
                    f"Line: {result.line['number']}"
                )

            if result.error:

                parts.append(
                    f"Error: {result.error['name']}"
                )

            result.summary = "\n".join(parts)

            result.confidence = 1.0

            result.reasoning = self.reasoner.think(result)

            result.decision = self.decision_engine.decide(result)

        return result