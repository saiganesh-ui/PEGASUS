"""
Close Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.close_action import CloseAction


class CloseSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.closer = CloseAction()

    def can_handle(self, decision):

        return decision["intent"] == "close"

    def execute(self, decision):

        app = decision["entity"]["app"]

        success = self.closer.execute(app)

        if success:

            self.context.set("last_app", app)
            self.context.set("last_command", decision["command"])

            return {

                "type": "response",

                "message": f"Closing {app}."

            }

        return {

            "type": "response",

            "message": f"I don't know how to close {app}."

        }