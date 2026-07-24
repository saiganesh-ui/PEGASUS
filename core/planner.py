"""
Planner
Project PEGASUS
"""

print(">>> LOADED NEW PLANNER <<<")

from modules.nlp.intent_classifier import IntentClassifier
from modules.nlp.entity_extractor import EntityExtractor
from modules.nlp.normalizer import Normalizer



class Planner:

    def __init__(self):

        self.classifier = IntentClassifier()
        self.extractor = EntityExtractor()
        self.normalizer = Normalizer()

    def plan(self, command):

        command = self.normalizer.normalize(command)

        print("Normalized:", command)   

        intent = self.classifier.classify(command)

        entity = self.extractor.extract(
            command,
            intent
        )

        return {
             
            "intent": intent,

            "entity": entity,

            "command": command,

            "confidence": 1.0 if intent != "unknown" else 0.0

        }