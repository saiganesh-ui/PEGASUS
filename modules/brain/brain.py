from .conversation import Conversation
from .patterns import PATTERNS


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
        for pattern in PATTERNS:

          if lower.startswith(pattern["prefix"]):

            value = text[len(pattern["prefix"]):].strip()

            return {
                    "type": "memory_store",
                     "key": pattern["key"],
                     "value": value
                  }
          
          if lower == "what is my name":
            return {
                "type": "memory_recall",
                "key": "name"
            }

        if lower == "what is my city":
            return {
                "type": "memory_recall",
                "key": "city"
            }

        if lower == "what is my favorite game":
            return {
                "type": "memory_recall",
                "key": "favorite_game"
            }

        if lower == "what is my college":
            return {
                "type": "memory_recall",
                "key": "college"
            }
        
        # Time
        if lower in [
          "what time is it",
          "time",
          "current time"
            ]:

            return {
                 "type": "time"
                }


        # Date
        if lower in [
             "what is today's date",
             "today's date",
            "date"
            ]:

            return {
                "type": "date"
                }


        # Day
        if lower in [
             "what day is today",
             "day"
        ]:

            return {
                "type": "day"
            }
        
        if lower == "system":

            return {"type":"system"}

        if lower == "cpu":

            return {"type":"cpu"}

        if lower == "memory":

            return {"type":"memory"}

        if lower == "ram":

            return {"type":"memory"}

        if lower == "disk":

            return {"type":"disk"}
        
        if lower.startswith("open "):

            app = text[5:].strip()

            return {

                "type": "open",

                "app": app

             }

        # Default
        return {
            "type": "command",
            "message": text
        }   