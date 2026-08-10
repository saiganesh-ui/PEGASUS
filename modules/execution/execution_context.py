"""
Execution Context
Project PEGASUS
Author: Sai Ganesh
"""


class ExecutionContext:

    def __init__(self):

        self.current_task = None
        self.last_result = None
        self.running = False