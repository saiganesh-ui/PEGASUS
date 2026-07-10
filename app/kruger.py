"""
KRUGER Core
Project PEGASUS
"""
from datetime import datetime
from modules.memory.memory import Memory



class Kruger:

    def __init__(self):
        self.version = "0.1"
        self.codename = "AWAKENING"
        self.status = "ONLINE"


        self.memory = Memory()

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

        

        self.memory.remember("favorite_game", "Spider-Man 2")
        
        self.memory.recall("favorite_game")

        print(f"\nStartup Time : {datetime.now()}")