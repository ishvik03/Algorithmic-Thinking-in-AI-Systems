import unittest
from window_manager import ContextWindowManager


class TestContextWindowManager(unittest.TestCase):

    def test_add_message_within_limit(self):
        manager = ContextWindowManager(max_tokens=10)

        manager.add_message("Hello", 3)
        manager.add_message("World", 4)

        self.assertEqual(manager.current_tokens, 7)
        self.assertEqual(manager.get_context(), ["Hello", "World"])

    def test_prune_when_exceeding_limit(self):
        manager = ContextWindowManager(max_tokens=10)

        manager.add_message("Hi", 2)
        manager.add_message("How are you?", 4)
        manager.add_message("Tell me a story", 6)

        # "Hi" should be removed to stay within token budget
        self.assertEqual(manager.current_tokens, 10)
        self.assertEqual(
            manager.get_context(),
            ["How are you?", "Tell me a story"]
        )

    def test_multiple_prunes(self):
        manager = ContextWindowManager(max_tokens=8)

        manager.add_message("A", 2)
        manager.add_message("B", 3)
        manager.add_message("C", 4)

        # Window should remove A and B
        self.assertEqual(manager.current_tokens, 4)
        self.assertEqual(manager.get_context(), ["C"])

    def test_empty_after_large_message(self):
        manager = ContextWindowManager(max_tokens=5)

        manager.add_message("Small", 2)
        manager.add_message("Too big", 10)

        # Only the large message remains after pruning
        self.assertEqual(manager.current_tokens, 10)
        self.assertEqual(manager.get_context(), ["Too big"])


if __name__ == "__main__":
    unittest.main()
