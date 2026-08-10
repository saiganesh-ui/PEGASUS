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
from modules.services.system_service import SystemService
from modules.actions.open_action import OpenAction
from modules.actions.open_folder_action import OpenFolderAction 
from modules.actions.search_action import SearchAction
from modules.actions.workspace_action import FileAction




class Kruger:

    def __init__(self):
        self.version = "0.1"
        self.codename = "AWAKENING"
        self.status = "ONLINE"


        self.memory = Memory()
        self.session = Session()
        self.time = TimeService() 
        self.system = SystemService()  
        self.opener = OpenAction()
        self.folder_opener = OpenFolderAction()
        self.search = SearchAction()
        self.files = FileAction()


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
            elif decision["type"] == "system":

                print(f"OS : {self.system.os_name()} {self.system.os_version()}")

                print(f"Processor : {self.system.processor()}")

                print(f"Machine : {self.system.machine()}")

                print(f"Python : {self.system.python_version()}")    

            elif decision["type"] == "cpu":

                print(f"CPU Usage : {self.system.cpu_usage()}%")      

            elif decision["type"] == "memory":

                ram = self.system.ram()

                print(f"RAM Usage : {ram.percent}%")

                print(f"Used : {ram.used//1024**3} GB")

                print(f"Total : {ram.total//1024**3} GB")

            elif decision["type"] == "disk":

                disk = self.system.disk()

                print(f"Used : {disk.used//1024**3} GB")

                print(f"Free : {disk.free//1024**3} GB")

                print(f"Total : {disk.total//1024**3} GB")  

            elif decision["type"] == "open":

                success = self.opener.execute(
                    decision["app"]
                )

                if success:

                    print(f"Opening {decision['app']}...")

                else:

                    print("Application not supported.")

            elif decision["type"] == "open_folder":

                success = self.folder_opener.execute(
                    decision["folder"]
                )

                if success:
                    print(f"Opening folder {decision['folder']}...")
                else:
                    print(f"I couldn't find folder {decision['folder']}.")

            elif decision["type"] == "search":

                self.search.execute(
                    decision["query"]
                )

                print(
                    f"Searching Google for '{decision['query']}'..."
                )

            elif decision["type"] == "create_folder":

                result = self.files.create_folder(
                    decision["name"]
                )

                print(result)

            elif decision["type"] == "create_file":

                result = self.files.create_file(
                    decision["name"]
                )

                print(result)

            elif decision["type"] == "delete_file":

                result = self.files.delete_file(
                    decision["name"]
                )

                print(result)   

            elif decision["type"] == "delete_folder":

                result = self.files.delete_folder(
                    decision["name"]
                )

                print(result)

            elif decision["type"] == "list_files":

                files = self.files.list_files()

                if not files:
                    print("Workspace is empty.")
                else:
                    print("\nWorkspace Files:")
                    for file in files:
                        print(f" - {file}")

            elif decision["type"] == "current_directory":

                 print(self.files.current_directory())