"""
Decision Engine
Project PEGASUS
Author: Sai Ganesh
"""


class DecisionEngine:

    def decide(self, result):

        # Error has highest priority
        if result.error:

            return (
                f"I detected a {result.error['name']}. "
                f"{result.error['message']}"
            )

        # Coding
        if result.screen_type == "code_editor":

            language = "Unknown"

            if result.language:
                language = result.language["name"]

            return (
                f"You are editing a {language} source file."
            )

        # Browser
        if result.screen_type == "browser":

            return "You are browsing the web."

        # Terminal
        if result.application:

            if result.application["name"] == "Terminal":

                return "You are working in the terminal."

        return "Screen analyzed successfully."