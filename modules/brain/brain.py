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
from modules.brain.decision_engine import DecisionEngine
from modules.router.handlers.system_handler import SystemHandler
from modules.router.handlers.open_handler import OpenHandler
from modules.router.handlers.search_handler import SearchHandler
from modules.router.handlers.file_handler import FileHandler
from modules.memory.memory import Memory


class Brain:

    def __init__(self):
        self.conversation = Conversation()
        self.normalizer = Normalizer()
        self.router = IntentRouter()
        self.memory = Memory()
        self.decision_engine = DecisionEngine()
 

        self.router.register("greeting", GreetingHandler())
        self.router.register("status", StatusHandler())
        self.router.register("search", SearchHandler())
        self.router.register("memory", MemoryHandler(self.memory))
        self.router.register("system", SystemHandler())
        self.router.register("open", OpenHandler())
        self.router.register("create_folder", FileHandler())
        self.router.register("create_file", FileHandler())
        self.router.register("delete_folder", FileHandler())
        self.router.register("delete_file", FileHandler())
        self.router.register("rename_folder", FileHandler())

    def think(self, command):
        if not command:
            return {"type": "command", "message": ""}

        text = command.strip()
        lower = self.normalizer.normalize(text)

        if lower in INTENTS["greeting"]:
            return self.router.execute("greeting")

        if lower in INTENTS["how_are_you"]:
           return self.router.execute("status")

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
            return {"type": "memory_recall", "key": "name"}

        if lower == "what is my city":
            return {"type": "memory_recall", "key": "city"}

        if lower == "what is my favorite game":
            return {"type": "memory_recall", "key": "favorite_game"}

        if lower == "what is my college":
            return {"type": "memory_recall", "key": "college"}

        if lower in ["what time is it", "time", "current time"]:
            return {"type": "time"}

        if lower in ["what is today's date", "today's date", "date"]:
            return {"type": "date"}

        if lower in ["what day is today", "day"]:
            return {"type": "day"}

        
        if lower in ("system", "cpu", "memory", "ram", "disk"):
                return {"type": lower}
            

                # Open folder
        if lower.startswith("open folder "):
            folder_name = text[len("open folder "):].strip()

            return {
                "type": "open_folder",
                "folder": folder_name
            }

        # Generic application opening
        for verb in INTENTS["open"]:
            if lower == verb or lower.startswith(verb + " "):
                app = text[len(verb):].strip() if lower != verb else ""
                return {
                    "type": "open",
                    "app": app or "default"
                }

        for prefix in INTENTS["search"]:
            if lower.startswith(prefix):
                query = text[len(prefix):].strip()
                return {"type": "search", "query": query}

        if lower.startswith("create folder "):
            folder_name = text[13:].strip()
            return {"type": "command", "message": f"create_folder {folder_name}"}

        if lower.startswith("create file "):
            file_name = text[12:].strip()
            return {"type": "command", "message": f"create_file {file_name}"}

        if lower.startswith("delete file "):
            file_name = text[12:].strip()
            return {"type": "delete_file", "name": file_name}

        if lower.startswith("delete folder "):
            folder_name = text[14:].strip()
            return {"type": "delete_folder", "name": folder_name}

        if lower.startswith("rename folder "):
            folder_name = text[14:].strip()
            return {"type": "rename_folder", "name": folder_name}

        if lower == "list files":
            return {"type": "list_files"}

        if lower in ["current directory", "pwd", "workspace"]:
            return {"type": "current_directory"}

        return {"type": "command", "message": text}
   