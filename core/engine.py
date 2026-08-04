"""
KRUGER Engine
Project PEGASUS
"""

from core.planner import Planner
from core.pipeline import Pipeline
from core.skill_manager import SkillManager
from modules.context.context import Context
from modules.scheduler.scheduler import Scheduler
from modules.scheduler.background_scheduler import BackgroundScheduler


class Engine:

    def __init__(self):

        self.context = Context()

        self.planner = Planner()

        self.scheduler = Scheduler()

        self.scheduler.load_saved_tasks()

        self.background_scheduler = BackgroundScheduler(
            self.scheduler
        )

        self.background_scheduler.start()

        self.skills = SkillManager(
            self.context,
            self.scheduler
        )

        self.pipeline = Pipeline(
            self.planner,
            self.skills,
            self.context
        )

    def process(self, command):

        return self.pipeline.run(command)