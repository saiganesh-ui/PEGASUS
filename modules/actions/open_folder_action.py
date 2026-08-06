"""
Open Folder Action
Project PEGASUS
"""

import subprocess
from modules.files.folder_resolver import FolderResolver


class OpenFolderAction:

    def __init__(self):

        self.resolver = FolderResolver()

    def execute(self, folder):

        folder = self.resolver.resolve(folder)

        if not folder:
            return False

        subprocess.Popen(["explorer", folder])

        return True