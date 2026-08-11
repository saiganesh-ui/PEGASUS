"""
Wake Word Service
Project PEGASUS
"""

import re


class WakeWordService:

    def __init__(self):

        self.words = [
            "kruger",
            "krugar",
            "krugarh",
            "kroger",
            "ruger",
            "roger",
            "rogar",
            "roja",
            "crewger",
            "krugers",
            "kruger's",
        ]

        self.fillers = [
            "hey",
            "okay",
            "ok",
            "hi",
            "hello",
            "yo"
        ]

    def process(self, text):

        text = text.lower()
        text = text.replace("'s", "s")
        text = text.replace("’s", "s")

        for word in self.words:

            if word not in text:
                continue

            # Remove wake word only once
            command = text.replace(word, "", 1)

            # Remove punctuation
            command = re.sub(
                r"^[\s,!.?:;-]+",
                "",
                command
            )

            command = re.sub(
                r"[\s,!.?:;-]+$",
                "",
                command
            )

            # Remove filler words left before the command
            for filler in self.fillers:

                pattern = rf"^{filler}[\s,!.?:;-]+"

                command = re.sub(
                    pattern,
                    "",
                    command,
                    count=1
                )

            command = command.strip()

            return {
                "wake": True,
                "command": command
            }

        return {
            "wake": False,
            "command": text
        }