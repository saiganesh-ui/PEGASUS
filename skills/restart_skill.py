"""
Restart Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.restart_action import RestartAction


class RestartSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.restarter = RestartAction()

    def can_handle(self, decision):

        return decision["intent"] == "restart"

    def execute(self, decision):

        app = decision["entity"]["app"]

        success = self.restarter.execute(app)

        if success:

            self.context.set("last_app", app)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"Restarting {app}."
            }

        return {
            "type": "response",
            "message": f"I don't know how to restart {app}."
        }