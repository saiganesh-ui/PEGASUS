import subprocess

class CloseAction:

    PROCESSES = {
        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "firefox": "firefox.exe",
        "vscode": "Code.exe",
        "code": "Code.exe",
        "notepad": "notepad.exe",
        "spotify": "Spotify.exe",
        "discord": "Discord.exe",
        "telegram": "Telegram.exe",
        "vlc": "vlc.exe",
        "calculator": "CalculatorApp.exe",
        "vscode": "Code.exe",
        "vs code": "Code.exe",
        "visual studio code": "Code.exe",
        "code": "Code.exe",
    }

    def execute(self, app):

        app = app.lower().strip()

        if app not in self.PROCESSES:
            print(f"Unknown app: {app}")
            return False

        process = self.PROCESSES[app]

        try:

            subprocess.run(
                ["taskkill", "/f", "/im", process],
                capture_output=True
            )

            print(f"Closed {app}")
            return True

        except Exception as e:

            print(f"Failed to close {app}: {e}")
            return False