"""
Entity Extractor
Project PEGASUS
"""

from modules.nlp.intents import PATTERNS


class EntityExtractor:

   def extract(self, command, intent):

    command = command.strip()

    if intent in ("unknown", "greeting", "how_are_you"):
        return None

    prefixes = PATTERNS.get(intent, [])

    for prefix in prefixes:

        if not command.lower().startswith(prefix.lower()):
            continue

        value = command[len(prefix):].strip()

        # OPEN
        if intent == "open":
            return {"app": value}

        # SEARCH
        if intent == "search":
            return {"query": value}

        # KNOWLEDGE
        if intent == "knowledge":
            return {}

        if intent == "forget":

            return {
                "key": value
            }

        # REMEMBER
        if intent == "remember":

            if prefix == "my name is ":
                return {"key": "name", "value": value}

            if prefix == "my city is ":
                return {"key": "city", "value": value}

            if prefix in ("my favorite game is ", "my favourite game is "):
                return {"key": "favorite_game", "value": value}

            if prefix == "my college is ":
                return {"key": "college", "value": value}

            if "=" in value:
                key, val = value.split("=", 1)
                return {
                    "key": key.strip().lower().replace(" ", "_"),
                    "value": val.strip()
                }

            if " is " in value:
                key, val = value.split(" is ", 1)
                return {
                    "key": key.strip().lower().replace(" ", "_"),
                    "value": val.strip()
                }

            return None

        # RECALL
        if intent == "recall":
            return {"key": value}

        # FILE
        if intent in (
            "create_folder",
            "create_file",
            "delete_folder",
            "delete_file",
            "rename_folder"
        ):
            return {"name": value}

        # SYSTEM
        if intent == "system":
            return {"command": command}

        elif intent == "weather":

            city = value.strip()

            if city.startswith("in "):

                city = city[3:]

            return {
                "city": city
            }

        # VISION
        elif intent == "vision":

            return {}

        # REMINDER
        if intent == "reminder":

            import re

            match = re.match(
                r"(.+?)\s+in\s+(\d+)\s+(second|seconds|minute|minutes|hour|hours|day|days)$",
                value,
                re.IGNORECASE
            )

            if not match:
                return {
                    "task": value,
                    "delay": 0,
                    "unit": "seconds"
                }

            return {
                "task": match.group(1).strip(),
                "delay": int(match.group(2)),
                "unit": match.group(3).lower()
            }

        return {"value": value}

    

    return None