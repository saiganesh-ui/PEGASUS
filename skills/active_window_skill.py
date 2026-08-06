"""
Active Window Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.active_window_action import ActiveWindowAction


class ActiveWindowSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.action = ActiveWindowAction()

    def can_handle(self, decision):

        return decision["intent"] == "active_window"

    def execute(self, decision):

        window = self.action.execute()

        if not window:

            return {

                "type": "response",

                "message": "I couldn't detect the active window."

            }

        return {

            "type": "response",

            "message": f"Active window: {window['title']}"

        }