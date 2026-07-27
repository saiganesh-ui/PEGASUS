"""
Entity Extractor
Project PEGASUS
"""

from modules.nlp.intents import PATTERNS


class EntityExtractor:

    def extract(self, command, intent):

        command = command.strip()

        if intent in ("unknown", "greeting"):
            return None

        prefixes = PATTERNS.get(intent, [])

        for prefix in prefixes:

            if command.lower().startswith(prefix.lower()):

                value = command[len(prefix):].strip()

                if intent == "open":
                    return {
                        "app": value
                    }

                elif intent == "search":
                    return {
                        "query": value
                    }

                elif intent == "remember":

                    if "=" not in value:
                        return None

                    key, val = value.split("=", 1)

                    return {
                        "key": key.strip(),
                        "value": val.strip()
                    }

                elif intent == "recall":

                    return {
                        "key": value
                    }

                elif intent in (
                    "create_folder",
                    "create_file",
                    "delete_folder",
                    "delete_file",
                    "rename_folder"
                ):

                    return {
                        "name": value
                    }

                elif intent == "system":

                    return {
                        "command": command
                    }

                return {
                    "value": value
                }

        return None