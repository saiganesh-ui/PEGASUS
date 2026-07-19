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

    def execute(self, command):

        for skill in self.skills:

            

            if skill.can_handle(command):

                return skill.execute(command)
        return None