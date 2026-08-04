"""
Execution Plan
Project PEGASUS
"""


class ExecutionPlan:

    def __init__(self):

        self.steps = []

    def add(self, action, entity):

        self.steps.append({
            "action": action,
            "entity": entity
        })

    def get_steps(self):

        return self.steps

    def clear(self):

        self.steps.clear()