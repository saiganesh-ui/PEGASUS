"""
Open Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.open_action import OpenAction


class OpenSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.opener = OpenAction()

    def can_handle(self, decision):

        return decision["intent"] == "open"

    def execute(self, decision):

        app = decision["entity"]["app"]

        success = self.opener.execute(app)

        if success:

            self.context.set("last_app", app)
            self.context.set("last_command", decision["command"])   

            return {
                "type": "response",
                "message": f"Opening {app}."
            }

        return {
            "type": "response",
            "message": f"I don't know how to open {app}."
        }