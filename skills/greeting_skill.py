"""
Greeting Skill
Project PEGASUS
"""

import random

from modules.nlp.intents import INTENTS
from modules.nlp.responses import RESPONSES

from skills.base_skill import BaseSkill


class GreetingSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

    def can_handle(self, text):

        return text in INTENTS["greeting"]

    def execute(self, command=None):

        return {
            "type": "response",
            "message": random.choice(
                RESPONSES["greeting"]
            )
        }