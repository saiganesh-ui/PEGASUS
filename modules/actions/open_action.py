"""
Open Action
Project PEGASUS
Author: Sai Ganesh
"""

import subprocess


class OpenAction:

    APPS = {

        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        "vscode": "code",

        "notepad": "notepad",

        "calculator": "calc",

        "explorer": "explorer"

    }

    def execute(self, app):

        app = app.lower()

        if app not in self.APPS:

            return False

        subprocess.Popen(self.APPS[app])

        return True