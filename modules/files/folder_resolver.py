"""
Folder Resolver
Project PEGASUS
"""

import os
from modules.files.folder_search import FolderSearch
from modules.files.folder_index import FolderIndex


class FolderResolver:

    def __init__(self):

        self.index = FolderIndex()

        self.index.load()

    def resolve(self, folder):

        folder = folder.strip()

        home = os.path.expanduser("~")

        known = {

            "desktop": os.path.join(home, "Desktop"),

            "downloads": os.path.join(home, "Downloads"),

            "documents": os.path.join(home, "Documents"),

            "pictures": os.path.join(home, "Pictures"),

            "music": os.path.join(home, "Music"),

            "videos": os.path.join(home, "Videos")

        }

        key = folder.lower()

        if key in known:

            return known[key]

        if os.path.isdir(folder):

            return folder

        return self.index.find(folder)


