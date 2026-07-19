"""
Skill Loader
Project PEGASUS
"""

import os
import importlib


class SkillLoader:

    def __init__(self, context):

        self.context = context

    def load(self):

        skills = []

        folder = "skills"

        for file in os.listdir(folder):

            if not file.endswith("_skill.py"):

                continue

            # Skip the abstract base class
            if file == "base_skill.py":

                continue

            module_name = file[:-3]

            module = importlib.import_module(

                f"skills.{module_name}"

            )

            class_name = "".join(

                word.capitalize()

                for word in module_name.replace(

                    "_skill",

                    ""

                ).split("_")

            ) + "Skill"

            cls = getattr(

                module,

                class_name

            )

            skills.append(

                cls(self.context)

            )
        return skills