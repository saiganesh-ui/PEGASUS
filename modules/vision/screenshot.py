"""
Screenshot
Project PEGASUS
"""

import pyautogui


class Screenshot:

    def capture(self, path="capture.png"):

        image = pyautogui.screenshot()

        image.save(path)

        return path