"""
KRUGER Memory Engine
"""

class Memory:

    def __init__(self):
        print("✓ Memory Engine Loaded")

    def remember(self, key, value):
        print(f"Remembering: {key} = {value}")

    def recall(self, key):
        print(f"Searching memory for '{key}'...")