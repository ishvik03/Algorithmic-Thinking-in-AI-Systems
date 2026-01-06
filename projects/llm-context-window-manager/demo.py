from window_manager import ContextWindowManager

def print_state(step, manager):
    print(f"\nStep {step}")
    print("Current context:")
    for msg in manager.get_context():
        print(f"  - {msg}")
    print(f"Total tokens in window: {manager.current_tokens}")

def main():
    # Imagine the LLM has a max context window of 10 tokens
    manager = ContextWindowManager(max_tokens=10)

    messages = [
        ("Hi", 2),
        ("How are you?", 4),
        ("Tell me a story", 6),
        ("Make it funny", 3),
    ]

    for i, (msg, tokens) in enumerate(messages, start=1):
        print(f"\nAdding message: '{msg}' ({tokens} tokens)")
        manager.add_message(msg, tokens)
        print_state(i, manager)

if __name__ == "__main__":
    main()
