"""
Intent Classifier
Project PEGASUS
"""

from modules.nlp.intents import INTENTS


class IntentClassifier:

    def classify(self, command):

        command = command.lower().strip()

        # Greeting
        if command in INTENTS["greeting"]:
            return "greeting"

        # Open App
        for prefix in INTENTS["open_app"]:
            if command.startswith(prefix):
                return "open"

        # Search
        for prefix in INTENTS["search"]:
            if command.startswith(prefix):
                return "search"

        # Memory
        for prefix in INTENTS["remember"]:
            if command.startswith(prefix):
                return "remember"

        for prefix in INTENTS["recall"]:
            if command.startswith(prefix):
                return "recall"

    
                # Create Folder
        for prefix in INTENTS["create_folder"]:

            if command.startswith(prefix):
                return "create_folder"

        # Create File
        for prefix in INTENTS["create_file"]:

            if command.startswith(prefix):
                return "create_file"

        # Delete Folder
        for prefix in INTENTS["delete_folder"]:

            if command.startswith(prefix):
                return "delete_folder"

        # Delete File
        for prefix in INTENTS["delete_file"]:

            if command.startswith(prefix):
                return "delete_file"

        # Rename Folder
        for prefix in INTENTS["rename_folder"]:

            if command.startswith(prefix):
                return "rename_folder"