"""
Skill Loader
Project PEGASUS
"""

import os
import importlib


class SkillLoader:

    def __init__(self, context, scheduler):

        self.context = context
        self.scheduler = scheduler

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

            try:

                print(f"Loaded: {class_name}")

                skills.append(

                    cls(
                        self.context,
                        self.scheduler
                    )

                )

            except Exception as e:

                print(f"Failed to load {class_name}: {e}")

        return skills        