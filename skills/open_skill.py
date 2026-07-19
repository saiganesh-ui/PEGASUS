"""
Open Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.open_action import OpenAction
from modules.nlp.intents import INTENTS
from modules.parser.command_parser import CommandParser


class OpenSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.opener = OpenAction()
        self.parser = CommandParser()


    def can_handle(self, command):

        prefixes = INTENTS["open_app"]

        command = command.lower()

        return any(
            command.startswith(prefix)
            for prefix in prefixes
        )

    def execute(self, command=None):

        prefixes = INTENTS["open_app"]

        app = self.parser.parse(command, prefixes)


        success = self.opener.execute(app)

        if success:

            self.context.set("last_app", app)

            self.context.set(

                "last_command",

                command

            )

            return {
                "type": "response",
                "message": f"Opening {app}."
            }

        return {
            "type": "response",
            "message": f"I don't know how to open {app}."
        }
