"""
Active Window Action
Project PEGASUS
Author: Sai Ganesh
"""

import pygetwindow as gw


class ActiveWindowAction:

    def execute(self):

        try:

            window = gw.getActiveWindow()

            if window is None:

                return None

            return {
                "title": window.title
            }

        except Exception:

            return None