"""
Time Skill
Project PEGASUS
"""

from datetime import datetime

from skills.base_skill import BaseSkill


class TimeSkill(BaseSkill):

    def can_handle(self, decision):

        return decision["intent"] in (
            "time",
            "date",
            "day"
        )

    def execute(self, decision):

        now = datetime.now()

        if decision["intent"] == "time":

            return {
                "type": "response",
                "message": now.strftime("%I:%M:%S %p")
            }

        elif decision["intent"] == "date":

            return {
                "type": "response",
                "message": now.strftime("%d %B %Y")
            }

        elif decision["intent"] == "day":

            return {
                "type": "response",
                "message": now.strftime("%A")
            }