"""
File Action
Project PEGASUS
"""

import os
import shutil
import time

WORKSPACE = os.path.join(os.getcwd(), "workspace")
os.makedirs(WORKSPACE, exist_ok=True)


class FileAction:

    def create_folder(self, name):

        path = os.path.join(WORKSPACE, name)

        os.makedirs(path, exist_ok=True)

        return f"Folder '{name}' created."
    
    def create_file(self, name):

        path = os.path.join(WORKSPACE, name)

        with open(path, "w") as file:
            pass

        return f"File '{name}' created."
    
    def delete_file(self, name):

        path = os.path.join(WORKSPACE, name)

        if os.path.exists(path):

            os.remove(path)

            return f"File '{name}' deleted."

        return f"File '{name}' not found."

    

    def delete_folder(self, name):

        path = os.path.join(WORKSPACE, name)

        if os.path.exists(path):

            time.sleep(2)

            shutil.rmtree(path)

            return f"Folder '{name}' deleted."

        return f"Folder '{name}' not found."
    

    def list_files(self):

        return os.listdir(WORKSPACE)
    
    def current_directory(self):

        return WORKSPACE