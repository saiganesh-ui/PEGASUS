"""
Running Applications Action
Project PEGASUS
"""

import win32gui


class RunningApplicationsAction:

    def execute(self):

        windows = []

        def callback(hwnd, extra):

            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd).strip()

            if not title:
                return

            # Chrome
            if "Google Chrome" in title:
                title = "Google Chrome"

            # VS Code
            elif "Visual Studio Code" in title:
                title = "Visual Studio Code"

            # Explorer
            elif title == "File Explorer":
                title = "File Explorer"

            # Notepad
            elif title.endswith("- Notepad"):
                title = "Notepad"

            # Discord
            elif "Discord" in title:
                title = "Discord"

            # Spotify
            elif "Spotify" in title:
                title = "Spotify"

            # Steam
            elif "Steam" in title:
                title = "Steam"

            # OBS
            elif "OBS" in title:
                title = "OBS Studio"

            if not title:
                return

            blacklist = {

                "Program Manager",
                "Settings",
                "Windows Input Experience"

            }

            if title in blacklist:
                return

            windows.append(title)

        win32gui.EnumWindows(callback, None)

        windows = sorted(set(windows))

        return windows