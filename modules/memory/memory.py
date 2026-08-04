from modules.memory.database import Database


class Memory:

    def __init__(self):

        self.database = Database()

        print("✓ Memory Engine Loaded")

    def remember(self, key, value):

        self.database.save_memory(key, value)

        print(f"Stored: {key}")

    def recall(self, key):

        result = self.database.get_memory(key)

        if result:

            print(f"{key} = {result[0]}")

            return result[0]

        print("Memory not found.")

        return None

    def get_all(self):
        return self.database.get_all()

    def delete(self, key):
        self.database.delete_memory(key)

    def clear(self):
        self.database.clear_memories()