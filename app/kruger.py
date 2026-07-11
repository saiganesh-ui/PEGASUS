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
from modules.services.time_service import TimeService




class Kruger:

    def __init__(self):
        self.version = "0.1"
        self.codename = "AWAKENING"
        self.status = "ONLINE"


        self.memory = Memory()
        self.session = Session()
        self.time = TimeService()   


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

            decision = self.brain.think(command)

            if decision["type"] == "response":

                print(decision["message"])

            elif decision["type"] == "command":

                self.command.execute(decision["message"])

            elif decision["type"] == "memory_store":

                self.memory.remember(
                     decision["key"],
                     decision["value"]
                )


                
                print(
                      f"I'll remember that your {decision['key']} is {decision['value']}."
                     )
            
            elif decision["type"] == "memory_recall":

                    self.memory.recall(
                        decision["key"]    
                    )
            elif decision["type"] == "time":

                print(
                     f"Current time: {self.time.current_time()}"
                    )


            elif decision["type"] == "date":

                print(
                     f"Today's date: {self.time.current_date()}"
                 )


            elif decision["type"] == "day":

                print(
                      f"Today is {self.time.current_day()}."
                    )        