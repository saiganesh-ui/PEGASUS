import unittest

from modules.brain.brain import Brain


class BrainTests(unittest.TestCase):
    def test_greeting_returns_response(self):
        brain = Brain()
        decision = brain.think("hello")

        self.assertEqual(decision["type"], "response")
        self.assertIn("message", decision)

    def test_memory_pattern_returns_memory_store_decision(self):
        brain = Brain()
        decision = brain.think("my name is Alex")

        self.assertEqual(decision["type"], "memory_store")
        self.assertEqual(decision["key"], "name")
        self.assertEqual(decision["value"], "Alex")


if __name__ == "__main__":
    unittest.main()
