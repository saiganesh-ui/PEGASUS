"""
Wake Word Service
Project PEGASUS
"""


class WakeWordService:

    def __init__(self):

        self.words = [

            "kruger",
            "krugar",
            "kurokar",
            "crewger",
            "krugarh"

        ]

    def process(self, text):

        text = text.lower()

        for word in self.words:

            if word in text:

                command = text.replace(word, "").strip()

                return {

                    "wake": True,

                    "command": command

                }

        return {

            "wake": False,

            "command": text

        }