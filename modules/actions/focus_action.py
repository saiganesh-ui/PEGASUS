"""
Focus Action
Project PEGASUS
"""

import win32gui
import win32con


class FocusAction:

    def execute(self, app):

        app = app.lower()

        target = None

        def callback(hwnd, extra):

            nonlocal target

            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd)

            if not title:
                return

            if app in title.lower():

                target = hwnd

        win32gui.EnumWindows(callback, None)

        if not target:
            return False

        # Restore if minimized
        win32gui.ShowWindow(target, win32con.SW_RESTORE)

        # Bring to front
        win32gui.SetForegroundWindow(target)

        return True