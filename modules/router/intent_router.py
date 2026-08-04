"""
Intent Router
Project PEGASUS
"""


class IntentRouter:

    def __init__(self):

        self.routes = {}

    def register(self, decision_type, handler):

        self.routes[decision_type] = handler

    def handle(self, decision):

        handler = self.routes.get(

            decision["type"]

        )

        if handler is None:

            return decision

        return handler.handle(decision)