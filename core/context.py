"""
Conversation Context
Project PEGASUS
"""


class Context:

    def __init__(self):

        self.data = {

            "last_app": None,

            "last_search": None,

            "last_file": None,

            "last_folder": None,

            "last_command": None

        }

    def set(self, key, value):

        self.data[key] = value

    def get(self, key):

        return self.data.get(key)

    def clear(self):

        self.data.clear()

    def all(self):

        return self.data