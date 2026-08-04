"""
Line Detector
Project PEGASUS
"""

import re


class LineDetector:

    def detect(self, text):

        match = re.search(r"line\s+(\d+)", text, re.IGNORECASE)

        if match:

            return match.group(1)

        return None