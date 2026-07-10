class CommandEngine:

    def __init__(self, memory):

        self.memory = memory

        print("✓ Command Engine Loaded")


    def execute(self, command):

        command = command.strip()

        if not command:
            return

        parts = command.split()

        action = parts[0].lower()


        if action == "remember":

            if len(parts) < 3:
                print("Usage: remember <key> <value>")
                return

            key = parts[1]
            value = " ".join(parts[2:])

            self.memory.remember(key, value)

            return


        if action == "recall":

            if len(parts) < 2:
                print("Usage: recall <key>")
                return

            key = parts[1]

            self.memory.recall(key)

            return


        print("Unknown command.")