"""
Memory Skill
Project PEGASUS
"""

from multiprocessing import context

from skills.base_skill import BaseSkill
from modules.memory.memory import Memory
from modules.nlp.intents import INTENTS
from modules.parser.command_parser import CommandParser


class MemorySkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.memory = Memory()
        self.parser = CommandParser()

    def can_handle(self, command):

        remember = any(
            command.startswith(prefix)
            for prefix in INTENTS["remember"]
        )

        recall = any(
            command.startswith(prefix)
            for prefix in INTENTS["recall"]
        )

        return remember or recall

    def execute(self, command=None):

        # Remember
        if any(command.startswith(prefix) for prefix in INTENTS["remember"]):

            key_value = self.parser.parse(
                command,
                INTENTS["remember"]
            )

            if "=" not in key_value:

                return {
                    "type": "response",
                    "message": "Use: remember key=value"
                }

            key, value = key_value.split("=", 1)

            self.memory.remember(
                key.strip(),
                value.strip()
            )

            return {
                "type": "response",
                "message": f"I'll remember your {key.strip()}."
            }

        # Recall
        key = self.parser.parse(
            command,
            INTENTS["recall"]
        )

        value = self.memory.recall(key)

        if value:

            return {

                "type": "response",

                "message": f"Your {key} is {value}."

            }

        return {

            "type": "response",

            "message": f"I don't know your {key}."

        }