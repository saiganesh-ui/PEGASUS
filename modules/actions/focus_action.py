from pywinauto import Application
from pywinauto.findwindows import find_windows

class FocusAction:

    TITLES = {
        "chrome": "Chrome",
        "edge": "Edge",
        "firefox": "Firefox",
        "vscode": "Visual Studio Code",
        "vs code": "Visual Studio Code",
        "visual studio code": "Visual Studio Code",
        "code": "Visual Studio Code",
        "notepad": "Notepad",
        "spotify": "Spotify",
        "discord": "Discord",
    }

    def execute(self, app):

        app = app.lower().strip()

        title = self.TITLES.get(app)

        if not title:
            print(f"Unknown app: {app}")
            return False

        try:
            handles = find_windows(title_re=f".*{title}.*")

            if not handles:
                print(f"No window found for {app}")
                return False

            app_obj = Application().connect(handle=handles[0])
            window = app_obj.window(handle=handles[0])

            window.restore()
            window.set_focus()

            print(f"Focused {app}")
            return True

        except Exception as e:
            print(f"Failed to focus {app}: {e}")
            return False