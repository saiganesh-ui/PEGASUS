"""
KRUGER Command Pipeline
Project PEGASUS
"""


class CommandPipeline:

    def __init__(self, brain, router):

        self.brain = brain
        self.router = router

    def process(self, command):

        decision = self.brain.think(command)

        if decision is None:

            return None

        return self.router.handle(decision)