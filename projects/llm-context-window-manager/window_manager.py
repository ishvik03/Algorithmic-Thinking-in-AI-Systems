class ContextWindowManager:
    def __init__(self, max_tokens):
        self.max_tokens = max_tokens
        self.messages = []
        self.current_tokens = 0

    def add_message(self, message, token_count):
        """
        Add a message and prune old context if token budget exceeded.
        """
        self.messages.append((message, token_count))
        self.current_tokens += token_count

        self._prune_if_needed()

    def _prune_if_needed(self):
        """
        Sliding window shrink step.
        Remove oldest messages until window is valid.
        """
        while self.current_tokens > self.max_tokens:
            _, tokens = self.messages.pop(0)
            self.current_tokens -= tokens

    def get_context(self):
        """
        Return messages currently inside the valid window.
        """
        return [msg for msg, _ in self.messages]
