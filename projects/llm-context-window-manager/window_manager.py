class ContextWindowManager:
    def __init__(self, max_tokens, debug=False):
        self.max_tokens = max_tokens
        self.messages = []  # (message, token_count, role, priority)
        self.current_tokens = 0
        self.debug = debug

    def add_message(self, message, token_count, role="user", priority=1):
        """
        Expand the window by adding a new message.
        """
        if self.debug:
            print(f"[ADD] {role.upper()} | tokens={token_count} | priority={priority}")
            print(f"      {message}")

        self.messages.append((message, token_count, role, priority))
        self.current_tokens += token_count

        self._prune_if_needed()

    def _prune_if_needed(self):
        """
        Sliding window shrink step with priority-aware pruning.
        """
        while self.current_tokens > self.max_tokens:
            # Remove lowest-priority message (oldest among equals)
            idx = min(
                range(len(self.messages)),
                key=lambda i: (self.messages[i][3], i)
            )

            removed_msg, tokens, role, priority = self.messages.pop(idx)
            self.current_tokens -= tokens

            if self.debug:
                print(
                    f"[PRUNE] Removed {role.upper()} | "
                    f"tokens={tokens} | priority={priority}"
                )
                print(f"[STATE] Current tokens: {self.current_tokens}")

    def get_context(self):
        """
        Return the active sliding window.
        """
        return [msg for msg, _, _, _ in self.messages]
