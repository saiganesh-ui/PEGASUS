"""
Skill Manager
Project PEGASUS
"""

from core.loader import SkillLoader
from modules import command


class SkillManager:

    def __init__(self, context):

        loader = SkillLoader(context)

        self.skills = loader.load()

    def execute(self, decision):

        for skill in self.skills:

            

            if skill.can_handle(decision):

                return skill.execute(decision)
        return None