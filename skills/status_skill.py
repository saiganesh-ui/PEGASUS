"""
Status Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class StatusSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

    def can_handle(self, decision):

        return decision["intent"] == "status"

    def execute(self, decision):

        data = self.context.all()

        if not data:
            return {
                "type": "response",
                "message": "Context is empty."
            }

        lines = []

        for key, value in data.items():

            lines.append(f"{key}: {value}")

        return {

            "type": "response",

            "message": "\n".join(lines)

        }