"""
Plugin Loader
Project PEGASUS
"""

import importlib
import inspect
import pkgutil

import skills
from skills.base_skill import BaseSkill


class PluginLoader:

    def load(self, context, scheduler):

        loaded = []

        for _, module_name, _ in pkgutil.iter_modules(skills.__path__):

            if module_name == "base_skill":
                continue

            module = importlib.import_module(
                f"skills.{module_name}"
            )

            for _, cls in inspect.getmembers(
                module,
                inspect.isclass
            ):

                if (
                    issubclass(cls, BaseSkill)
                    and cls != BaseSkill
                ):

                    try:

                        loaded.append(
                            cls(
                                context,
                                scheduler
                            )
                        )

                    except TypeError:

                        loaded.append(
                            cls(context)
                        )

        return loaded