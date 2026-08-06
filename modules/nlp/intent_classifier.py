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

        # How are you
        if command in PATTERNS["how_are_you"]:
            return "how_are_you"

        # OPEN FOLDER
        for prefix in PATTERNS["open_folder"]:
            if command.startswith(prefix):
                 return "open_folder"

        # Open App
        for prefix in PATTERNS["open"]:
            if command.startswith(prefix):
                return "open"


        # Close App
        for prefix in PATTERNS["close"]:
            if command.startswith(prefix):
                return "close"

        # Restart App
        for prefix in PATTERNS["restart"]:
            if command.startswith(prefix):
                return "restart"

        # Running Applications
        if command in PATTERNS["running_apps"]:
            return "running_apps"

        # Focus Application
        for prefix in PATTERNS["focus"]:
            if command.startswith(prefix):
                return "focus"

        #ACTIVE WINDOW
        if command in PATTERNS["active_window"]:
            return "active_window"

        #WHAT AM I DOING
        if command in PATTERNS["what_am_i_doing"]:
            return "what_am_i_doing"

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

        # Knowledge

        for phrase in PATTERNS["knowledge"]:

            if command == phrase:
                return "knowledge"

        for prefix in PATTERNS["forget"]:
            if command.startswith(prefix):
                return "forget"

        

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

        if command in PATTERNS["time"]:
            return "time"

        if command in PATTERNS["date"]:
            return "date"

        if command in PATTERNS["day"]:
            return "day"

        # Reminder
        for prefix in PATTERNS["reminder"]:
            if command.startswith(prefix):
                return "reminder"

        # Weather
        for prefix in PATTERNS["weather"]:
            if command.startswith(prefix):
                return "weather"

        # Vision    
        if command in PATTERNS["vision"]:
            return "vision"    

        # Help
        if command in PATTERNS["help"]:

            return "help"

        return "unknown"