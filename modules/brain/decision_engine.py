"""
Decision Engine
Project PEGASUS

Creates a structured decision object from
the NLP pipeline output.
"""


class DecisionEngine:

    def decide(self, command, intent, entity):

        if intent == "how_are_you":
            intent = "status"

        return {
            "intent": intent,
            "entity": entity,
            "command": command,
            "confidence": 1.0 if intent != "unknown" else 0.0
        }