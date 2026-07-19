"""
Memory Handler
Project PEGASUS
"""

from modules.router.base_handler import BaseHandler


class MemoryHandler(BaseHandler):

    def __init__(self, memory):

        self.memory = memory

    def execute(self, decision):

        self.memory.remember(

            decision["key"],

            decision["value"]

        )

        return {

            "type": "response",

            "message": f"I'll remember that your {decision['key']} is {decision['value']}."

        }