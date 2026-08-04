"""
Command Pipeline
Project PEGASUS
"""

from modules.nlp.reference_resolver import ReferenceResolver
from modules.nlp.command_splitter import CommandSplitter
from modules.services.voice_service import VoiceService


class Pipeline:

    def __init__(self, planner, skills, context):

        self.planner = planner
        self.skills = skills
        self.context = context

        self.reference_resolver = ReferenceResolver(context)

        self.command_splitter = CommandSplitter()

        self.voice = VoiceService()

    def run(self, command):

        commands = self.command_splitter.split(command)

        results = []

        for command in commands:

            command = self.reference_resolver.resolve(command)

            self.context.add_history(command)

            plan = self.planner.plan(command)

            print(plan)

            import traceback

            try:
                result = self.skills.execute(plan)

            except Exception:

                traceback.print_exc()
                raise

            results.append(result)

        responses = []

        for result in results:

            if result:

                message = result.get("message")

                if message:

                    self.voice.speak(message)

                responses.append(result)

        return responses
                    