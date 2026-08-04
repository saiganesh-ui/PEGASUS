"""
Search Handler
Project PEGASUS
"""


class SearchHandler:

    def handle(self, decision):

        return {
            "type": "search",
            "decision": decision
        }