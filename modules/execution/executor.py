"""
Executor
Project PEGASUS
Author: Sai Ganesh
"""

from modules.execution.action_result import ActionResult


class Executor:

    def execute(self, task):

        result = ActionResult()

        result.success = True

        result.action = task.intent

        result.target = task.target

        result.message = "Execution completed."

        return result