import random

from .conversation import Conversation
from .patterns import PATTERNS
from modules.nlp.normalizer import Normalizer
from modules.nlp.intents import INTENTS
from modules.nlp.responses import RESPONSES
from modules.router.intent_router import IntentRouter
from modules.router.handlers.greeting_handler import GreetingHandler
from modules.router.handlers.status_handler import StatusHandler
from modules.router.handlers.memory_handler import MemoryHandler


class Brain:

    def __init__(self):

        self.conversation = Conversation()
        self.normalizer = Normalizer()

        self.router = IntentRouter()

        self.router.register(
            "greeting",
            GreetingHandler()
        )

        self.router.register(
            "status",
            StatusHandler()
            )
        
        self.router.register(

            "memory",

            MemoryHandler(self.memory)

            )

    def think(self, command):

        text = command.strip()
        lower = self.normalizer.clean(text)

        # Greetings
        if lower in INTENTS["greeting"]:

            return self.router.execute(
                "greeting"
            )
        
        if lower in INTENTS["how_are_you"]:

            return self.router.execute(
                "status"
            )

        # Natural Language Memory
       # Natural Language Memory
        for pattern in PATTERNS:

            if lower.startswith(pattern["prefix"]):

                value = text[len(pattern["prefix"]):].strip()

                decision = {

                    "key": pattern["key"],

                    "value": value

                }

                return self.router.execute(

                    "memory",

                    decision

                )
          
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
        
        for verb in INTENTS["open_app"]:

            if lower.startswith(verb + " "):

                app = text[len(verb):].strip()

                if app.startswith("google "):
                    app = app[7:]

                return {

                    "type":"open",

                    "app":app

                }
        
        if lower.startswith(("search ", "google ")):

            if lower.startswith("search "):
                query = text[7:].strip()
            else :
                query = text[7:].strip()

            return {
                    "type": "search",
                    "query": query
            }
        
        if lower.startswith("create folder "):

            folder_name = text[14:].strip()

            return {
                "type": "create_folder",
                "name": folder_name
            }
        
        if lower.startswith("create file "):

            file_name = text[12:].strip()

            return {
                "type": "create_file",
                "name": file_name
            }
        
        if lower.startswith("delete file "):

            file_name = text[12:].strip()

            return {
                "type": "delete_file",
                "name": file_name
            }

        if lower.startswith("delete folder "):

            folder_name = text[14:].strip()

            return {
                "type": "delete_folder",
                "name": folder_name
            }
        
        if lower == "list files":

            return {
                "type": "list_files"
            }
        
        if lower in ["current directory", "pwd", "workspace"]:

            return {
                "type": "current_directory"
            }

        # Default
        return {
            "type": "command",
            "message": text
        }   