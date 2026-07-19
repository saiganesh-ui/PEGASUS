"""
Command Registry
Project PEGASUS
"""


class CommandRegistry:

    def __init__(self):

        self.commands = {}

    def register(self, command, handler):

        self.commands[command] = handler

    def execute(self, command):

        handler = self.commands.get(command)

        if handler:

            return handler()

        return None