"""
Weather Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class WeatherSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

    def can_handle(self, decision):

        return decision["intent"] == "weather"

    def execute(self, decision):

        city = "your location"

        entity = decision.get("entity")

        if entity and "city" in entity:

            city = entity["city"]

        return {
            "type": "response",
            "message": f"Weather service is not connected yet for {city}."
        }