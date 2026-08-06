"""
Folder Index
Project PEGASUS
Author: Sai Ganesh
"""

import os
import json


class FolderIndex:

    INDEX_FILE = "data/folder_index.json"

    def __init__(self):

        self.index = {}

    def build(self):

        home = os.path.expanduser("~")

        self.index.clear()

        for root, dirs, files in os.walk(home):

            for folder in dirs:

                key = folder.lower()

                if key not in self.index:

                    self.index[key] = os.path.join(root, folder)

        self.save()

    def save(self):

        os.makedirs("data", exist_ok=True)

        with open(self.INDEX_FILE, "w", encoding="utf-8") as file:

            json.dump(
                self.index,
                file,
                indent=4
            )

    def load(self):

        if not os.path.exists(self.INDEX_FILE):

            self.build()

            return

        with open(self.INDEX_FILE, "r", encoding="utf-8") as file:

            self.index = json.load(file)

    def find(self, folder_name):

        if not self.index:

            self.load()

        return self.index.get(folder_name.lower())