"""
Action Result
Project PEGASUS
Author: Sai Ganesh
"""


class ActionResult:

    def __init__(self):

        self.success = False
        self.action = None
        self.target = None
        self.message = None
        self.execution_time = 0.0
        self.details = {}