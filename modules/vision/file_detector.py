"""
Python File Detector
Project PEGASUS
"""

import re


class FileDetector:

    def detect(self, text):

        match = re.search(r"\b[\w\-]+\.py\b", text)

        if match:

            return {
                "name": match.group(),
                "confidence": 1.0
            }

        return None