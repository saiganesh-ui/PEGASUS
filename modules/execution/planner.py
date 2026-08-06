"""
Planner
Project PEGASUS
Author: Sai Ganesh
"""

from modules.execution.task import Task


class Planner:

    def plan(self, decision):

        task = Task()

        task.intent = decision["intent"]

        task.target = decision.get("entity", {})

        task.steps.append("execute")

        return task

    