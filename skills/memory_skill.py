"""
Memory Skill
Project PEGASUS
"""



from skills.base_skill import BaseSkill
from modules.memory.memory import Memory

class MemorySkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.memory = Memory()

    def can_handle(self, decision):

        return decision["intent"] in (
            "remember",
            "recall"
        )
    def execute(self, decision):

        intent = decision["intent"]
        entity = decision["entity"]

        # Remember
        if intent == "remember":

            if "=" not in entity:

                return {
                    "type": "response",
                    "message": "Use: remember key=value"
                }

            key, value = entity.split("=", 1)

            key = key.strip()
            value = value.strip()

            self.memory.remember(key, value)

            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"I'll remember your {key}."
            }

        # Recall
        key = entity.strip()

        value = self.memory.recall(key)

        self.context.set("last_command", decision["command"])

        if value:

            return {
                "type": "response",
                "message": f"Your {key} is {value}."
            }

        return {
            "type": "response",
            "message": f"I don't know your {key}."
        }