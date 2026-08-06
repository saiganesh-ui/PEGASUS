"""
Running Applications Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.running_applications_action import RunningApplicationsAction


class RunningApplicationsSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.runner = RunningApplicationsAction()

    def can_handle(self, decision):

        return decision["intent"] == "running_apps"

    def execute(self, decision):

        apps = self.runner.execute()

        if not apps:

            return {
                "type": "response",
                "message": "No running applications found."
            }

        text = "\n".join(apps[:25])

        return {
            "type": "response",
            "message": "Running Applications:\n\n" + text
        }