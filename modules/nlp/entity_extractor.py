"""
Entity Extractor
Project PEGASUS
"""

from modules.nlp.intents import PATTERNS


class EntityExtractor:

    def extract(self, command, intent):

        command = command.strip()

        if intent == "unknown":
            return None

        if intent == "greeting":
            return None

        # Find prefixes for this intent
        prefixes = PATTERNS.get(intent, [])

        for prefix in prefixes:

            if command.lower().startswith(prefix.lower()):

                entity = command[len(prefix):].strip()

                return entity if entity else None

        return None