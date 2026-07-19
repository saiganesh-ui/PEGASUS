"""
Command Parser
Project PEGASUS
"""


class CommandParser:

    def parse(self, command, prefixes):

        for prefix in prefixes:

            if command.startswith(prefix):

                return command[len(prefix):].strip()

        return None