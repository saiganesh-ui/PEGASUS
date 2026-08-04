"""
System Handler
Project PEGASUS
"""


class SystemHandler:

    def handle(self, decision=None):

        command = decision["command"]

        if command == "system":
            return {"type": "system"}

        elif command == "cpu":
            return {"type": "cpu"}

        elif command in ("memory", "ram"):
            return {"type": "memory"}

        elif command == "disk":
            return {"type": "disk"}

        return {
            "type": "response",
            "message": "Unknown system command."
        }