"""
Running Applications Action
Project PEGASUS
"""

import psutil


class RunningAppsAction:

    def execute(self):

        apps = []

        for process in psutil.process_iter(["name"]):

            try:

                name = process.info["name"]

                if not name:
                    continue

                name = name.lower()

                if name.endswith(".exe"):
                    name = name[:-4]

                # Skip Windows background processes
                blacklist = {

                    "svchost",
                    "dllhost",
                    "conhost",
                    "fontdrvhost",
                    "registry",
                    "csrss",
                    "lsass",
                    "services",
                    "wininit",
                    "smss",
                    "system",
                    "idle"

                }

                if name in blacklist:
                    continue

                apps.append(name)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                pass

        apps = sorted(set(apps))

        return apps