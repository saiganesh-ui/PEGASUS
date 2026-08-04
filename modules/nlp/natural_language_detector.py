"""
Natural Language Detector
Project PEGASUS
"""

import re


class NaturalLanguageDetector:

    PATTERNS = [

        (
            re.compile(r"my (.+?) is (.+)", re.IGNORECASE),
            lambda m: (
                "remember",
                {
                    "key": m.group(1).strip().lower().replace(" ", "_"),
                    "value": m.group(2).strip()
                }
            )
        ),

        (
            re.compile(r"i study at (.+)", re.IGNORECASE),
            lambda m: (
                "remember",
                {
                    "key": "college",
                    "value": m.group(1).strip()
                }
            )
        ),

        (
            re.compile(r"i use (.+)", re.IGNORECASE),
            lambda m: (
                "remember",
                {
                    "key": "tool",
                    "value": m.group(1).strip()
                }
            )
        ),
    
        (
            re.compile(r"what(?:'s| is) my (.+)", re.IGNORECASE),
            lambda m: (
                "recall",
                {
                    "key": m.group(1).strip().lower().replace(" ", "_")
                }
            )
        ),

        (
            re.compile(r"who am i", re.IGNORECASE),
            lambda m: (
                "recall",
                {
                    "key": "name"
                }
            )
        ),

        (
            re.compile(r"where do i study", re.IGNORECASE),
            lambda m: (
                "recall",
                {
                    "key": "college"
                }
            )
        ),

        (
            re.compile(r"where am i from", re.IGNORECASE),
            lambda m: (
                "recall",
                {
                    "key": "city"
                }
            )
        ),

        (
            re.compile(r"what laptop do i have", re.IGNORECASE),
            lambda m: (
                "recall",
                {
                    "key": "laptop"
                }
            )
        ),


    ]

    def detect(self, command):

        for pattern, handler in self.PATTERNS:

            match = pattern.fullmatch(command)

            if match:

                intent, entity = handler(match)

                return {
                    "intent": intent,
                    "entity": entity
                }

        return None