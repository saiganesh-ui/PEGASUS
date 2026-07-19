"""
KRUGER Engine
Project PEGASUS
"""

from core.planner import Planner
from core.pipeline import Pipeline
from core.skill_manager import SkillManager
from core.context import Context


class Engine:

    def __init__(self):

        self.context = Context()

        self.planner = Planner()

        self.skills = SkillManager(self.context)

        self.pipeline = Pipeline(
            self.planner,
            self.skills,
            self.context
        )

    def process(self, command):

        return self.pipeline.run(command)