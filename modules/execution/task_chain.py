"""
Task Chain
Project PEGASUS
Author: Sai Ganesh
"""


class TaskChain:

    def __init__(self):

        self.steps = []

    def add(self, action):

        self.steps.append(action)

    def __iter__(self):

        return iter(self.steps)

    def __len__(self):

        return len(self.steps)