"""
Open Action
Project PEGASUS
Author: Sai Ganesh
"""

import subprocess


class OpenAction:

    APPS = {

        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        "vscode": r"C:\Program Files\Microsoft VS Code\Code.exe",

        "notepad": "notepad",

        "calculator": "calc",

        "explorer": "explorer"

    }

    def execute(self, app):

        app = app.lower()

        if app not in self.APPS:
            return False

        if app == "chrome":

            subprocess.Popen([
                self.APPS["chrome"],
                "--profile-directory=Default"
            ])

        else:

            subprocess.Popen(self.APPS[app])

        return True