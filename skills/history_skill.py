"""
History Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class HistorySkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

    def can_handle(self, decision):

        return decision["intent"] == "history"

    def execute(self, decision):

        app = self.context.get("last_app")

        if app:

            return {

                "type": "response",

                "message": f"The last app you opened was {app}."

            }

        return {

            "type": "response",

            "message": "You haven't opened any application yet."

        }