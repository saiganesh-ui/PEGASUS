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
        entity = decision["entity"]

        # Create Folder
        if intent == "create_folder":

            self.file.create_folder(entity)

            self.context.set("last_folder", entity)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"Folder '{entity}' created."
            }

        # Create File
        elif intent == "create_file":

            self.file.create_file(entity)

            self.context.set("last_file", entity)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"File '{entity}' created."
            }

        # Delete Folder
        elif intent == "delete_folder":

            self.file.delete_folder(entity)

            self.context.set("last_folder", entity)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"Folder '{entity}' deleted."
            }

        # Delete File
        elif intent == "delete_file":

            self.file.delete_file(entity)

            self.context.set("last_file", entity)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"File '{entity}' deleted."
            }

        # Rename Folder (placeholder)
        elif intent == "rename_folder":

            return {
                "type": "response",
                "message": "Rename folder is not implemented yet."
            }

        return {
            "type": "response",
            "message": "Unknown file command."
        }