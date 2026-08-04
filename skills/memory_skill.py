"""
Memory Skill
Project PEGASUS
"""



from skills.base_skill import BaseSkill
from modules.memory.memory import Memory
from modules.brain.memory_judge import MemoryJudge


class MemorySkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        super().__init__(context)

        self.judge = MemoryJudge()
        self.memory = Memory()

    def can_handle(self, decision):

        return decision["intent"] in (
            "remember",
            "recall",
            "knowledge",
            "forget"
        )
    
    def execute(self, decision):

        intent = decision["intent"]

        # Remember
        if intent == "remember":

            key = decision["entity"]["key"]
            value = decision["entity"]["value"]

            if self.judge.should_store(key, value):

                self.memory.remember(key, value)

            else:

                return {

                    "type": "response",

                    "message": "I don't think this needs to be remembered."

                }
            self.context.set("last_topic", key)
            self.context.set("last_command", decision["command"])

            return {
                "type": "response",
                "message": f"I'll remember your {key}."
            }

        # Recall
        elif intent == "recall":

            key = decision["entity"]["key"]

            self.context.set("last_topic", key)

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

        elif intent == "knowledge":

            memories = self.memory.get_all()

            if not memories:
                return {
                    "type": "response",
                    "message": "I don't know anything about you yet."
                }

            text = "Here's what I know about you:\n\n"

            for key, value in memories:
                text += f"{key.replace('_',' ').title()}: {value}\n"

            return {
                "type": "response",
                "message": text
            }

        elif intent == "forget":

            key = decision["entity"]["key"]

            self.context.set("last_topic", key)

            if key == "all":

                self.memory.clear()

                return {
                    "type": "response",
                    "message": "All memories have been deleted."
                }

            self.memory.delete(key)

            return {
                "type": "response",
                "message": f"I forgot your {key}."
            }