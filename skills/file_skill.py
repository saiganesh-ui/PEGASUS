"""
File Skill
Project PEGASUS
"""

from modules import command
from skills.base_skill import BaseSkill
from modules.actions.file_action import FileAction
from modules.nlp.intents import INTENTS
from modules.parser.command_parser import CommandParser


class FileSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.file = FileAction()
        self.parser = CommandParser()

    def can_handle(self, command):

        command = command.lower()

        file_intents = [

            "create_folder",
            "create_file",
            "delete_folder",
            "delete_file",
            "rename_folder"

        ]

        for intent in file_intents:

            for prefix in INTENTS[intent]:

                if command.startswith(prefix):
                    return True

        return False

    def execute(self, command=None):

        # Create Folder
        if command.startswith("create folder "):

            folder = self.parser.parse(
                command,
                ["create folder "]
            )

            self.file.create_folder(folder)

            self.context.set("last_folder", folder)
            self.context.set("last_command", command)

            return {
                "type": "response",
                "message": f"Folder '{folder}' created."
            }

        # Create File
        elif command.startswith("create file "):

            filename = self.parser.parse(
                command,
                ["create file "]
            )

            self.file.create_file(filename)

            self.context.set("last_file", filename)
            self.context.set("last_command", command)

          

            return {
                "type": "response",
                "message": f"File '{filename}' created."
            }

        # Delete Folder
        elif command.startswith("delete folder "):

            folder = self.parser.parse(
                command,
                ["delete folder "]
            )

            self.file.delete_folder(folder)

            self.context.set("last_folder", folder)
            self.context.set("last_command", command)

            return {
                "type": "response",
                "message": f"Folder '{folder}' deleted."
            }

        # Delete File
        elif command.startswith("delete file "):

            filename = self.parser.parse(
                command,
                ["delete file "]
            )

            self.file.delete_file(filename)
            self.context.set("last_file", filename)
            self.context.set("last_command", command)

            return {
                "type": "response",
                "message": f"File '{filename}' deleted."
            }

        return {
            "type": "response",
            "message": "Unknown file command."
        }