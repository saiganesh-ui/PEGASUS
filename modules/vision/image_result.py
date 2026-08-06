"""
Image Result
Project PEGASUS
Author: Sai Ganesh
"""


class ImageResult:

    def __init__(self):

        # Image Information
        self.path = None
        self.width = 0
        self.height = 0
        self.format = None
        self.mode = None

        # OCR
        self.text = ""

        # Detection Results
        self.application = None
        self.file = None
        self.language = None
        self.line = None
        self.error = None

        # Analysis
        self.summary = None
        self.screen_type = None
        self.confidence = 0.0
        self.reasoning = []
        self.decision = None

    def to_dict(self):

        return {

            "path": self.path,
            "width": self.width,
            "height": self.height,
            "format": self.format,
            "mode": self.mode,
            "reasoning": self.reasoning,
            "decision": self.decision,
            "text": self.text,

            "application": self.application,
            "file": self.file,
            "language": self.language,
            "line": self.line,
            "error": self.error,

            "summary": self.summary,
            "screen_type": self.screen_type,
            "confidence": self.confidence

        }

    def __str__(self):

        lines = []

        if self.application:
            lines.append(f"Application : {self.application['name']}")

        if self.file:
            lines.append(f"File : {self.file['name']}")

        if self.language:
            lines.append(f"Language : {self.language['name']}")

        if self.line:
            lines.append(f"Line : {self.line['number']}")

        if self.error:
            lines.append(f"Error : {self.error['name']}")
            lines.append(self.error["message"])

        return "\n".join(lines)