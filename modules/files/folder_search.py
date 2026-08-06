"""
Folder Search
Project PEGASUS
Author: Sai Ganesh
"""

import os


class FolderSearch:

    def __init__(self):

        self.home = os.path.expanduser("~")

    def search(self, folder_name):

        folder_name = folder_name.lower().strip()

        try:

            for root, dirs, files in os.walk(self.home):

                for directory in dirs:

                    if directory.lower() == folder_name:

                        return os.path.join(root, directory)

        except Exception:

            return None

        return None