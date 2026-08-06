"""
Application Detector
Project PEGASUS
"""


class AppDetector:

    APPS = {

        "visual studio code": "Visual Studio Code",

        "chrome": "Google Chrome",

        "powershell": "PowerShell",

        "terminal": "Terminal",

        "explorer": "File Explorer",

        "cmd": "Command Prompt",

        "notepad": "Notepad",

        "paint": "Paint",

        "calculator": "Calculator",

        "spotify": "Spotify",

        "word": "Microsoft Word",

        "excel": "Microsoft Excel",

        "powerpoint": "Microsoft PowerPoint",

        "outlook": "Microsoft Outlook",

        "teams": "Microsoft Teams",

        "edge": "Microsoft Edge",

        "firefox": "Mozilla Firefox",

        "safari": "Safari",

        "photoshop": "Adobe Photoshop",

        "illustrator": "Adobe Illustrator",

        "premiere": "Adobe Premiere Pro",

        "after effects": "Adobe After Effects",

        "blender": "Blender",

        "unity": "Unity",

        "unreal engine": "Unreal Engine",

        "vscode": "Visual Studio Code",

        "pycharm": "PyCharm",

        "intellij": "IntelliJ IDEA",

        "android studio": "Android Studio",

        "eclipse": "Eclipse",

        "netbeans": "NetBeans",

        "chatgpt": "ChatGPT",

        "midjourney": "MidJourney",

        "dalle": "DALL·E",

        "stable diffusion": "Stable Diffusion",

        "gpt-4": "GPT-4",

        "gpt-3": "GPT-3",

        "gpt-2": "GPT-2",

        "gpt-1": "GPT-1",

        "openai": "OpenAI",

        "huggingface": "Hugging Face",

        "youtube": "YouTube",

        "netflix": "Netflix",

        "hulu": "Hulu",

        "disney plus": "Disney+",

        "prime video": "Amazon Prime Video",

        "twitch": "Twitch",

        "steam": "Steam",

        "epic games": "Epic Games",

        "gimp": "GIMP",

        "vlc": "VLC Media Player",

        "skype": "Skype",

        "zoom": "Zoom",

        "slack": "Slack",

        "discord": "Discord",

        "telegram": "Telegram",

        "whatsapp": "WhatsApp",

        "signal": "Signal",

        "line": "LINE",

        "wechat": "WeChat",

        "viber": "Viber",

        "kodi": "Kodi",

        "obs": "OBS Studio",

        "audacity": "Audacity",

        "settings": "Settings",

        "control panel": "Control Panel",

        "task manager": "Task Manager",

        "file explorer": "File Explorer",

        "system": "System",

        "weather": "Weather",

        "reminder": "Reminder",

        "calendar": "Calendar",

        "clock": "Clock",

        "maps": "Maps",

        "instagram": "Instagram",

        "facebook": "Facebook",

        "twitter": "Twitter",

        "linkedin": "LinkedIn",

        "reddit": "Reddit",

        "armory crate": "Armory Crate",

        "steam deck": "Steam Deck",

        "epic games launcher": "Epic Games Launcher",

        "": "Unknown"



    }

    def detect(self, text):

        text = text.lower()

        for keyword, app in self.APPS.items():

            if keyword in text:

                return {
                    "name": app,
                    "confidence": 1.0
                }

        return None