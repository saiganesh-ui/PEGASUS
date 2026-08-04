"""
Status Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class StatusSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)


    def can_handle(self, decision):

        return decision["intent"] == "status"

    def execute(self, decision):

        data = self.context.all()

        if not data:
            return {
                "type": "response",
                "message": "Context is empty."
            }

        labels = {
            "last_app": "Last App",
            "last_search": "Last Search",
            "last_file": "Last File",
            "last_folder": "Last Folder",
            "last_command": "Last Command"
        }

        lines = []

        for key, value in data.items():

            label = labels.get(key, key)

            lines.append(f"{label}: {value}")

        return {

            "type": "response",

            "message": "\n".join(lines)

        }