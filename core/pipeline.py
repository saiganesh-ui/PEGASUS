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

            # -----------------------------------------
            # COMMAND -> DECISION
            # -----------------------------------------

            decision = self.planner.plan(command)

            # -----------------------------------------
            # CONFIDENCE SAFETY GATE
            # -----------------------------------------

            if not decision.get("approved", True):

                result = {
                    "type": "response",
                    "message": decision.get(
                        "message",
                        "I'm not confident enough to execute that command."
                    )
                }

                results.append(result)

                continue

            # -----------------------------------------
            # EXECUTE SKILL
            # -----------------------------------------

            result = self.skills.execute(decision)

            if result:

                results.append(result)

        # -----------------------------------------
        # RESPONSES
        # -----------------------------------------

        responses = []

        for result in results:

            if result:

                message = result.get("message")

                if message:

                    self.voice.speak(message)

                responses.append(result)

        return responses