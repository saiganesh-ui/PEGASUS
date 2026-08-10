"""
How Are You Skill
Project PEGASUS
"""

import random

from modules.nlp.responses import RESPONSES
from skills.base_skill import BaseSkill


class HowAreYouSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(
            context,
            scheduler
        )

    def can_handle(self, decision):

        return decision["intent"] == "how_are_you"

    def execute(self, decision):

        return {
            "type": "response",
            "message": random.choice(
                RESPONSES["how_are_you"]
            )
        }