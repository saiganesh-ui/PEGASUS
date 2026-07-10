"""
KRUGER Core
Project PEGASUS
"""
from datetime import datetime
from modules.memory.memory import Memory 
from modules.command.command_engine import CommandEngine
from modules.brain.brain import Brain
from modules.logger.logger import Logger
from modules.memory.session import Session




class Kruger:

    def __init__(self):
        self.version = "0.1"
        self.codename = "AWAKENING"
        self.status = "ONLINE"


        self.memory = Memory()
        self.session = Session()


        self.command = CommandEngine(self.memory)
        self.brain = Brain()
        self.logger = Logger()

    def startup(self):
        self.logger.info("KRUGER Starting")
        print("=" * 50)
        print(f"        KRUGER v{self.version}")
        print(f"         {self.codename}")
        print("=" * 50)

        print("\nInitializing...")

        print("✓ Configuration Loaded")
        print("✓ Memory  Initialized")
        self.logger.info("Memory Engine Loaded")
        print("✓ Modules Loaded")
        self.logger.info("Modules Loaded")

        print("\nHello, Ganesh.")

        print("KRUGER is online.")

        print("Awaiting command...")

        self.session.set("status", "Running")
        self.session.set("user", "Ganesh")

        print(self.session.get("status"))
        print(self.session.get("user"))

        
        while True:

            command = input("\nKRUGER > ")

            if command.lower() == "exit":

                print("Goodbye, Ganesh.")

                break

            response = self.brain.think(command)

            if response:

                 print(response)

            else:

                self.command.execute(command)
    