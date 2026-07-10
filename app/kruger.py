"""
KRUGER Core
Project PEGASUS
"""
from datetime import datetime
from modules.memory.memory import Memory 
from modules.command.command_engine import CommandEngine



class Kruger:

    def __init__(self):
        self.version = "0.1"
        self.codename = "AWAKENING"
        self.status = "ONLINE"


        self.memory = Memory()


        self.command = CommandEngine(self.memory)

    def startup(self):

        print("=" * 50)
        print(f"        KRUGER v{self.version}")
        print(f"         {self.codename}")
        print("=" * 50)

        print("\nInitializing...")

        print("✓ Configuration Loaded")
        print("✓ Memory  Initialized")
        print("✓ Modules Loaded")

        print("\nHello, Ganesh.")

        print("KRUGER is online.")

        print("Awaiting command...")

        
        while True:

            command = input("\nKRUGER > ")

            if command.lower() == "exit":

                print("Goodbye, Ganesh.")

                break

            self.command.execute(command)

    