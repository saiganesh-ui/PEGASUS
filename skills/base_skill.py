"""
Base Skill
Project PEGASUS
"""


class BaseSkill:

    def __init__(self, context, scheduler=None):

        self.context = context
        self.scheduler = scheduler

    def can_handle(self, decision):
        raise NotImplementedError

    def execute(self, decision):
        raise NotImplementedError