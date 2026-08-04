"""
Python File Detector
Project PEGASUS
"""

import re


class FileDetector:

    def detect(self, text):

        match = re.search(r"\b[\w\-]+\.py\b", text)

        if match:

            return match.group()

        return None