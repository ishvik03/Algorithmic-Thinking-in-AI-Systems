from window_manager import ContextWindowManager

def run_demo():
    manager = ContextWindowManager(max_tokens=50, debug=True)

    manager.add_message(
        "You are a helpful assistant.",
        token_count=10,
        role="system",
        priority=3
    )

    manager.add_message(
        "Hi, can you help me with Python?",
        token_count=12,
        role="user",
        priority=2
    )

    manager.add_message(
        "Sure! What do you need help with?",
        token_count=10,
        role="assistant",
        priority=1
    )

    manager.add_message(
        "Explain sliding window algorithms.",
        token_count=15,
        role="user",
        priority=2
    )

    manager.add_message(
        "Here is a detailed explanation of sliding windows...",
        token_count=20,
        role="assistant",
        priority=1
    )

    print("\nFinal Context Sent to LLM:")
    for msg in manager.get_context():
        print("-", msg)

if __name__ == "__main__":
    run_demo()
