"""
Execution Engine
Project PEGASUS
Author: Sai Ganesh
"""

from modules.execution.executor import Executor
from modules.execution.verifier import Verifier


class ExecutionEngine:

    def __init__(self):

        self.executor = Executor()
        self.verifier = Verifier()

    def execute(self, task):

        result = self.executor.execute(task)

        verified = self.verifier.verify(result)

        return result, verified