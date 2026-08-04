"""
Planner
Project PEGASUS
"""

print(">>> LOADED NEW PLANNER <<<")

from modules.nlp.intent_classifier import IntentClassifier
from modules.nlp.entity_extractor import EntityExtractor
from modules.nlp.normalizer import Normalizer
from modules.brain.decision_engine import DecisionEngine
from modules.nlp.natural_language_detector import NaturalLanguageDetector
from modules.brain.execution_plan import ExecutionPlan


class Planner:

    def __init__(self):

        self.classifier = IntentClassifier()
        self.extractor = EntityExtractor()
        self.normalizer = Normalizer()
        self.decision_engine = DecisionEngine()
        self.nl = NaturalLanguageDetector()
        self.execution_plan = ExecutionPlan()
    def plan(self, command):

        command = self.normalizer.normalize(command)

        natural = self.nl.detect(command)

        if natural:

            intent = natural["intent"]
            entity = natural["entity"]

        else:

            intent = self.classifier.classify(command)
            entity = self.extractor.extract(command, intent)

        self.execution_plan.clear()

        self.execution_plan.add(
            intent,
            entity
        )

        return self.decision_engine.decide(
            command,
            intent,
            entity
        )