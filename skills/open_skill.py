"""
Open Skill
Project PEGASUS
"""

from modules.execution.planner import ExecutionPlanner
from modules.execution.executor import Executor


class OpenSkill:

    def __init__(self, context, scheduler=None):

        self.context = context
        self.scheduler = scheduler

        self.planner = ExecutionPlanner()
        self.executor = Executor()

    def can_handle(self, decision):

        return decision.get("intent") == "open"

    def execute(self, decision):

        task = self.planner.plan(decision)

        result = self.executor.execute(task)

        return {
            "type": "response",
            "message": result.message
        }