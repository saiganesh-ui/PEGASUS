from .conversation import Conversation


class Brain:

    def __init__(self):

        self.conversation = Conversation()

    def think(self, command):

        text = command.strip()
        lower = text.lower()

        # Greetings
        if lower in ["hello", "hi", "hey"]:
            return {
                "type": "response",
                "message": "Hello, Ganesh."
            }

        if lower == "how are you":
            return {
                "type": "response",
                "message": "I'm operating normally."
            }

        # Natural Language Memory
        if lower.startswith("my name is "):

            name = text[11:].strip()

            return {
                "type": "memory_store",
                "key": "name",
                "value": name
            }

        # Default
        return {
            "type": "command",
            "message": text
        }   