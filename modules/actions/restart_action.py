"""
Restart Action
Project PEGASUS
"""

import time

from modules.actions.open_action import OpenAction
from modules.actions.close_action import CloseAction


class RestartAction:

    def __init__(self):

        self.opener = OpenAction()
        self.closer = CloseAction()

    def execute(self, app):

        success = self.closer.execute(app)

        if not success:
            return False

        time.sleep(1)

        return self.opener.execute(app)