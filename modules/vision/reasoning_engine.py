"""
Reasoning Engine
Project PEGASUS
Author: Sai Ganesh
"""


class ReasoningEngine:

    def think(self, result):

        thoughts = []

        # Application
        if result.application:

            app = result.application["name"]

            if app == "Visual Studio Code":
                thoughts.append("You are writing or editing code.")

            elif app == "Google Chrome":
                thoughts.append("You are browsing the web.")

            elif app == "Terminal":
                thoughts.append("You are using the command line.")

            elif app == "File Explorer":
                thoughts.append("You are managing files.")

        # Language
        if result.language:

            thoughts.append(
                f"The detected programming language is {result.language['name']}."
            )

        # Error
        if result.error:

            thoughts.append(
                f"A {result.error['name']} is visible."
            )

            thoughts.append(
                result.error["message"]
            )

        return thoughts