"""
Command Splitter
Project PEGASUS
"""


class CommandSplitter:

    def split(self, command):

        separators = (

    " and then ",

    " then ",

    " afterwards ",

    " after that ",

    " next ",

    " also ",

    " as well as ",

    " along with ",

    " and ",

    ","

)

        commands = [command]

        for separator in separators:

            temp = []

            for cmd in commands:

                temp.extend(cmd.split(separator))

            commands = temp

        return [
            cmd.strip()
            for cmd in commands
            if cmd.strip()
        ]