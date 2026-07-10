"""
KRUGER Brain
Project PEGASUS
"""

class Brain:

    def think(self, command):

        command = command.lower()

        if "hello" in command:
            return "Hello, Ganesh."

        if "hi" in command:
            return "Hi, Ganesh."

        if "how are you" in command:
            return "I'm operating normally."

        return None