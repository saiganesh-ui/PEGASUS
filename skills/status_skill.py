"""
Status Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class StatusSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

    def can_handle(self, command):

        command = command.lower()

        return command in [

            "status",

            "context",

            "history"

        ]

    def execute(self, command=None):

        data = self.context.all()

        lines = []

        for key, value in data.items():

            lines.append(f"{key}: {value}")

        return {

            "type": "response",

            "message": "\n".join(lines)

        }