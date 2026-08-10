"""
Activity Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.vision.vision import Vision


class ActivitySkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.vision = Vision()

    def can_handle(self, decision):

        return decision["intent"] == "what_am_i_doing"

    def execute(self, decision):

        result = self.vision.analyze_screen()

        return {

            "type": "response",

            "message": result.decision

        }