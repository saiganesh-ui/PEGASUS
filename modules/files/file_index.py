"""
File Index
Project PEGASUS
Author: Sai Ganesh
"""

import os
import json


class FileIndex:

    INDEX_FILE = "data/file_index.json"

    def __init__(self):

        self.index = {}

    def build(self):

        home = os.path.expanduser("~")

        self.index.clear()

        for root, dirs, files in os.walk(home):

            for file in files:

                key = file.lower()

                if key not in self.index:

                    self.index[key] = os.path.join(root, file)

        self.save()

    def save(self):

        os.makedirs("data", exist_ok=True)

        with open(self.INDEX_FILE, "w", encoding="utf-8") as f:

            json.dump(
                self.index,
                f,
                indent=4
            )

    def load(self):

        if not os.path.exists(self.INDEX_FILE):

            self.build()

            return

        with open(self.INDEX_FILE, "r", encoding="utf-8") as f:

            self.index = json.load(f)

    def find(self, filename):

        if not self.index:

            self.load()

        return self.index.get(filename.lower())