"""
Vision Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill

from modules.vision.screenshot import Screenshot
from modules.vision.ocr import OCR
from modules.vision.error_detector import ErrorDetector
from modules.vision.app_detector import AppDetector
from modules.vision.file_detector import FileDetector
from modules.vision.line_detector import LineDetector


class VisionSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.screenshot = Screenshot()
        self.ocr = OCR()
        self.detector = ErrorDetector()
        self.app_detector = AppDetector()
        self.file_detector = FileDetector()
        self.line_detector = LineDetector()

    def can_handle(self, decision):

        return decision["intent"] == "vision"

    def execute(self, decision):

        path = self.screenshot.capture()

        text = self.ocr.read(path)

        app = self.app_detector.detect(text)

        file = self.file_detector.detect(text)

        line = self.line_detector.detect(text)

        error = self.detector.detect(text)

        if not text.strip():

            return {
                "type": "response",
                "message": "I couldn't detect any readable text."
            }

        message = ""

        message += f"Application : {app}\n"

        if file:
            message += f"Python File : {file}\n"

        if line:
            message += f"Line : {line}\n"

        if error:

            message += f"\nError : {error['error']}\n"

            message += f"{error['explanation']}"

        else:

            message += "\nNo known Python error detected."

        return {

            "type": "response",

            "message": message

        }
    

        