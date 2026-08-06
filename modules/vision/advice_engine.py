"""
Advice Engine
Project PEGASUS
Author: Sai Ganesh
"""


class AdviceEngine:

    def advise(self, result):

        advice = []

        if result.error:

            error = result.error["name"]

            if error == "ModuleNotFoundError":

                advice.append(
                    "Check whether the module is installed."
                )

                advice.append(
                    "Verify the import statement."
                )

            elif error == "SyntaxError":

                advice.append(
                    "Review the highlighted line for syntax mistakes."
                )

            elif error == "IndentationError":

                advice.append(
                    "Check your indentation levels."
                )

        if result.application:

            if result.application["name"] == "Terminal":

                advice.append(
                    "You can rerun the command after fixing the issue."
                )

        return advice