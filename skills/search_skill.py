"""
Search Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill
from modules.actions.search_action import SearchAction
from modules.nlp.intents import INTENTS
from modules.parser.command_parser import CommandParser


class SearchSkill(BaseSkill):

    def __init__(self, context):

        super().__init__(context)

        self.search = SearchAction()
        self.parser = CommandParser()

    def can_handle(self, command):

        prefixes = INTENTS["search"]

        return any(
            command.startswith(prefix)
            for prefix in prefixes
        )

    def execute(self, command=None):

        prefixes = INTENTS["search"]

        query = self.parser.parse(command, prefixes)

        self.search.execute(query)

        self.context.set("last_search", query)
        self.context.set("last_command", command)

        return {

            "type": "response",

            "message": f"Searching Google for '{query}'."

        }