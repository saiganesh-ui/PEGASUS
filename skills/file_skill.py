"""
File Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.file_action import FileAction


class FileSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.file = FileAction()

    def can_handle(self, decision):

        return decision["intent"] in (
            "create_folder",
            "create_file",
            "delete_folder",
            "delete_file",
            "rename_folder"
        )

    def execute(self, decision):

        intent = decision["intent"]
        name = decision["entity"]["name"]

        if intent == "create_folder":

            self.file.create_folder(name)

            self.context.set("last_folder", name)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"Folder '{name}' created."
            }

        elif intent == "create_file":

            self.file.create_file(name)

            self.context.set("last_file", name)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"File '{name}' created."
            }

        elif intent == "delete_folder":

            self.file.delete_folder(name)

            self.context.set("last_folder", name)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"Folder '{name}' deleted."
            }

        elif intent == "delete_file":

            self.file.delete_file(name)

            self.context.set("last_file", name)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"File '{name}' deleted."
            }

        elif intent == "rename_folder":

            return {
                "type": "response",
                "message": "Rename folder is not implemented yet."
            }

        return {
            "type": "response",
            "message": "Unknown file command."
        }