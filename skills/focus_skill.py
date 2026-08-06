"""
Focus Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.focus_action import FocusAction


class FocusSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.focus = FocusAction()

    def can_handle(self, decision):

        return decision["intent"] == "focus"

    def execute(self, decision):

        app = decision["entity"]["app"]

        success = self.focus.execute(app)

        if success:

            self.context.set("last_app", app)

            return {
                "type": "response",
                "message": f"Focusing {app}."
            }
        

        return {
            "type": "response",
            "message": f"I couldn't find {app}."
        }
    