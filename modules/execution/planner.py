"""
Execution Planner
Project PEGASUS
Author: Sai Ganesh
"""

from modules.execution.task import Task


class ExecutionPlanner:

    def plan(self, decision):

        task = Task()

        task.intent = decision["intent"]
        task.target = decision.get("entity", {})

        if task.intent == "open":

            task.steps = [
                "validate",
                "open",
                "verify"
            ]

        elif task.intent == "close":

            task.steps = [
                "validate",
                "close",
                "verify"
            ]

        elif task.intent == "focus":

            task.steps = [
                "find_window",
                "focus",
                "verify"
            ]

        elif task.intent == "restart":

            task.steps = [
                "close",
                "wait",
                "open",
                "verify"
            ]

        else:

            task.steps = [
                "execute"
            ]

        return task