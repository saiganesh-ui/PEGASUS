"""
Reference Resolver
Project PEGASUS
"""


class ReferenceResolver:

    def __init__(self, context):

        

        self.context = context

    def resolve(self, command):

        command = command.lower().strip()

        if command in ("open it", "open it again"):

            app = self.context.get("last_app")

            if app:
                return f"open {app}"
            
        if command in ("search it", "search it again"):

            query = self.context.get("last_search")

            if query:
                return f"search {query}"

        if command == "delete it":

            file_name = self.context.get("last_file")
            if file_name:
                return f"delete file {file_name}"

            folder = self.context.get("last_folder")
            if folder:
                return f"delete folder {folder}"

   

        if command == "recall it":

            topic = self.context.get("last_topic")

            if topic:
                return f"recall {topic}"

        if command == "forget it":

            topic = self.context.get("last_topic")

            if topic:
                return f"forget {topic}"

        return command