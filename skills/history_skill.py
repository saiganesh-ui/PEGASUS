"""
History Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class HistorySkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)
        super().__init__(context)

    def can_handle(self, decision):
        return decision["intent"] == "history"

    def execute(self, decision):

        history = self.context.get_history()

        if not history:
            return {
                "type": "response",
                "message": "No command history available."
            }

        lines = ["Recent Commands:"]

        for index, command in enumerate(history, start=1):
            lines.append(f"{index}. {command}")

        return {
            "type": "response",
            "message": "\n".join(lines)
        }