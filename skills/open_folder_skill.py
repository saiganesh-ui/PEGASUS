"""
Open Folder Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.open_folder_action import OpenFolderAction


class OpenFolderSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.action = OpenFolderAction()

    def can_handle(self, decision):

        return decision["intent"] == "open_folder"

    def execute(self, decision):

        folder = decision["entity"]["folder"]

        success = self.action.execute(folder)

        if success:

            return {
                "type": "response",
                "message": f"Opening folder {folder}."
            }

        return {
            "type": "response",
            "message": f"I couldn't find folder {folder}."
        }