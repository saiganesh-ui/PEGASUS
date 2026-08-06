"""
Close Action
Project PEGASUS
"""

import subprocess


class CloseAction:

    def __init__(self):

        self.apps = {

            "chrome": "chrome.exe",

            "vscode": "Code.exe",

            "notepad": "notepad.exe",

            "calculator": "CalculatorApp.exe"

        }

    def execute(self, app):

        if app not in self.apps:

            return False

        try:

            subprocess.run(

                [

                    "taskkill",

                    "/IM",

                    self.apps[app],

                    "/F"

                ],

                stdout=subprocess.DEVNULL,

                stderr=subprocess.DEVNULL

            )

            return True

        except Exception:

            return False