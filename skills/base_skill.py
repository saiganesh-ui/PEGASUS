"""
Base Skill
Project PEGASUS
"""


class BaseSkill:

    def __init__(self, context):

        self.context = context

    def can_handle(self, command):

        raise NotImplementedError

    def execute(self, command):

        raise NotImplementedError