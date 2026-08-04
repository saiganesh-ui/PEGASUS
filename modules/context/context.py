class Context:

    def __init__(self):

        self.data = {
            "last_app": None,
            "last_search": None,
            "last_file": None,
            "last_folder": None,
            "last_command": None
        }

        self.history = []

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def all(self):
        return self.data

    def add_history(self, command):

        self.history.append(command)

        # Keep only the latest 20 commands
        if len(self.history) > 20:
            self.history.pop(0)

    def get_history(self):
        return self.history