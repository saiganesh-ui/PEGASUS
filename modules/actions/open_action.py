import os
import subprocess
import psutil

from modules.actions.focus_action import FocusAction

class OpenAction:

    APPS = {
        # Browsers
        "chrome": r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default"',
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",

        # Editors
        "vscode": r"C:\Program Files\Microsoft VS Code\Code.exe",
        "vs code": r"C:\Program Files\Microsoft VS Code\Code.exe",
        "visual studio code": r"C:\Program Files\Microsoft VS Code\Code.exe",
        "code": r"C:\Program Files\Microsoft VS Code\Code.exe",
        
        "notepad": "notepad.exe",

        # Media
        "spotify": r"C:\Users\%USERNAME%\AppData\Roaming\Spotify\Spotify.exe",
        "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",

        # Communication
        "discord": r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "telegram": r"C:\Users\%USERNAME%\AppData\Roaming\Telegram Desktop\Telegram.exe",
        "whatsapp": r"whatsapp.exe",

        # Utilities
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
        "explorer": "explorer.exe",
        "task manager": "taskmgr.exe",
    }

    PROCESS_NAMES = {
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "vscode": "Code.exe",
    "vs code": "Code.exe",
    "visual studio code": "Code.exe",
    "code": "Code.exe",
    "notepad": "notepad.exe",
    "spotify": "Spotify.exe",
    "discord": "Discord.exe",
}

    def execute(self, app):

        app = app.lower().strip()

        if app not in self.APPS:
            print(f"Unknown app: {app}")
            return False, f"I couldn't find or open the application '{app}'."

        # -------------------------------------------------
        # Check if already running
        # -------------------------------------------------

        process_name = self.PROCESS_NAMES.get(app)

        if process_name:

            for proc in psutil.process_iter(["name"]):

                try:
                    if proc.info["name"] and proc.info["name"].lower() == process_name.lower():

                        FocusAction().execute(app)

                        print(f"{app} already running; focused existing window")

                        return True, f"{app} is already running. Focusing it."

                except Exception:
                    pass

        # -------------------------------------------------
        # Open application
        # -------------------------------------------------

        path = os.path.expandvars(self.APPS[app])

        try:

            if " --processStart " in path:
                subprocess.Popen(path, shell=True)
            else:
                subprocess.Popen(path)

            print(f"Opened {app}")
            return True, f"Opening {app}."

        except Exception as e:

            print(f"Failed to open {app}: {e}")
            return False, f"I couldn't find or open the application '{app}'."