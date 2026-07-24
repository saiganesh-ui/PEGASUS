"""
Intent Classifier
Project PEGASUS
"""

from modules.nlp.intents import PATTERNS


class IntentClassifier:

    def classify(self, command):

        command = command.lower().strip()

        # Greeting
        if command in PATTERNS["greeting"]:
            return "greeting"

        # Open App
        for prefix in PATTERNS["open"]:
            if command.startswith(prefix):
                return "open"

        # Search
        for prefix in PATTERNS["search"]:
            if command.startswith(prefix):
                return "search"

        # Memory
        for prefix in PATTERNS["remember"]:
            if command.startswith(prefix):
                return "remember"

        for prefix in PATTERNS["recall"]:
            if command.startswith(prefix):
                return "recall"

    
                # Create Folder
        for prefix in PATTERNS["create_folder"]:

            if command.startswith(prefix):
                return "create_folder"

        # Create File
        for prefix in PATTERNS["create_file"]:

            if command.startswith(prefix):
                return "create_file"

        # Delete Folder
        for prefix in PATTERNS["delete_folder"]:

            if command.startswith(prefix):
                return "delete_folder"

        # Delete File
        for prefix in PATTERNS["delete_file"]:

            if command.startswith(prefix):
                return "delete_file"

        # Rename Folder
        for prefix in PATTERNS["rename_folder"]:

            if command.startswith(prefix):
                return "rename_folder"

        if command in PATTERNS["system"]:
            return "system"

        if command in PATTERNS["status"]:
            return "status"

        if command in PATTERNS["history"]:
            return "history"    

                    
        return "unknown"        