"""
Vision Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill

from modules.vision.screenshot import Screenshot
from modules.vision.ocr import OCR
from modules.vision.screen_analyzer import ScreenAnalyzer

class VisionSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.screenshot = Screenshot()
        self.ocr = OCR()
        self.analyzer = ScreenAnalyzer()

    def can_handle(self, decision):

        return decision["intent"] == "vision"

    def execute(self, decision):

        path = self.screenshot.capture()

        text = self.ocr.read(path)

        if not text.strip():

            return {
                "type": "response",
                "message": "I couldn't detect any readable text."
            }

        result = self.analyzer.analyze(text)

        message = ""

        if result.application:
            message += f"Application : {result.application['name']}\n"

        if result.file:
            message += f"File : {result.file['name']}\n"

        if result.language:
            message += f"Language : {result.language['name']}\n"

        if result.line:
            message += f"Line : {result.line['number']}\n"

        if result.error:
            message += f"\nError : {result.error['name']}\n"
            message += f"{result.error['message']}\n"

        if result.reasoning:

            message += "\nReasoning:\n"

            for thought in result.reasoning:

                message += f"- {thought}\n"

            message += "\nDecision:\n"
            message += result.decision

        if result.advice:

            message += "\nAdvice:\n"

            for item in result.advice:

                message += f"- {item}\n"
        
        else:
            message += "\nNo known error detected."

        return {
            "type": "response",
            "message": message
        }
    

        