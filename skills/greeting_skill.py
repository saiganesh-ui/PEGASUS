"""
Greeting Skill
Project PEGASUS
"""

import random

from modules.nlp.intents import PATTERNS
from modules.nlp.responses import RESPONSES

from skills.base_skill import BaseSkill


class GreetingSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        super().__init__(context)

    def can_handle(self, decision):

        return decision["intent"] == "greeting"

    def execute(self, decision):

        return {
            "type": "response",
            "message": random.choice(
                RESPONSES["greeting"]
            )
        }