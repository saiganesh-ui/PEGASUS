"""
Command Pipeline
Project PEGASUS
"""


class Pipeline:

    def __init__(self, planner, skills, context):

        self.planner = planner

        self.skills = skills

        self.context = context

    def run(self, command):

        plan = self.planner.create_plan(command)

        result = self.skills.execute(plan)

        return result