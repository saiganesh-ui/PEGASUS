"""
System Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.services.system_service import SystemService
from core.registry import CommandRegistry


class SystemSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.system = SystemService()

        self.registry = CommandRegistry()

        self.registry.register("cpu", self.system.cpu)
        self.registry.register("memory", self.system.memory)
        self.registry.register("ram", self.system.memory)
        self.registry.register("disk", self.system.disk)
        self.registry.register("storage", self.system.disk)
        self.registry.register("system info", self.system.system_info)

    def can_handle(self, decision):

        return decision["intent"] == "system"

    def execute(self, decision):

        command = decision["entity"] or decision["command"]

        result = self.registry.execute(command.lower())

        if result:
            return {    
                "type": "response",
                "message": result
            }

        return {
            "type": "response",
            "message": "Unknown system command."
        }