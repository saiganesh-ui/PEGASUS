"""
Confidence Engine
Project PEGASUS
"""


class ConfidenceEngine:

    def score(self, intent, entity):

        if intent == "unknown":
            return 0.0

        if entity is None:
            return 0.8

        return 1.0