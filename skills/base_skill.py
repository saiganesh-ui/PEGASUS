"""
Base Skill
Project PEGASUS
"""


class BaseSkill:

    def __init__(self, context):

        self.context = context

    def can_handle(decision):

        raise NotImplementedError

    def execute(decision):

        raise NotImplementedError