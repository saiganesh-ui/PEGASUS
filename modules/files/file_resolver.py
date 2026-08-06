"""
File Resolver
Project PEGASUS
"""

import os

from modules.files.file_index import FileIndex


class FileResolver:

    def __init__(self):

        self.index = FileIndex()

        self.index.load()

    def resolve(self, filename):

        filename = filename.strip()

        if os.path.isfile(filename):

            return filename

        return self.index.find(filename)