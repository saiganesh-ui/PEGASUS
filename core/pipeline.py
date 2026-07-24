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

        plan = self.planner.plan(command)

        print(plan)

        result = self.skills.execute(
            plan
        )
        return result