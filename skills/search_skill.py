"""
Search Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.search_action import SearchAction


class SearchSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.search = SearchAction()

    def can_handle(self, decision):

        return decision["intent"] == "search"

    def execute(self, decision):

        query = decision["entity"]

        self.search.execute(query)

        self.context.set("last_search", query)
        self.context.set("last_command", decision["command"])

        return {

            "type": "response",

            "message": f"Searching Google for '{query}'."

        }