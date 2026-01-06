## LLM Context Window Manager
### Overview

Large Language Models operate under strict token limits, making naïve context truncation unreliable in real-world applications. This project implements a **context-aware memory manager** that applies **sliding window algorithms** to maintain relevant conversation history while enforcing token constraints.

Instead of arbitrarily dropping messages, the system incrementally expands and prunes context using clear validity rules, resulting in stable, predictable, and production-ready LLM behavior.

### Problem Statement

In production systems, conversation history grows unbounded while model context windows remain fixed. Common strategies like “last-N messages” often discard critical information, causing hallucinations, loss of coherence, and poor user experience.

This project reframes context management as a **constrained window optimization problem**, inspired by classic sliding window techniques from algorithm design.

### Core Idea

Conversation history is treated as a **variable-size sliding window**:

1. The window expands as new messages arrive

2. The window shrinks when token limits are exceeded

3. Validity is defined by total token count

4. Memory updates reuse prior computation instead of rebuilding context

This mirrors sliding window patterns used in problems like longest valid substring or minimum window optimization.

### System Design

1. Incoming messages are appended to a conversation buffer

2. Token usage is tracked incrementally

3. When the token budget is exceeded, oldest messages are removed until the window becomes valid

4. The resulting window is passed to the LLM as context

This guarantees the model always receives a valid and coherent context.

### Why Sliding Window?

Sliding window logic is a natural fit because:

1. Context depends on a contiguous sequence of messages

2. Constraints can be checked incrementally

3. Recomputing context from scratch is inefficient

### Key Features

1. Token-aware context management

2. Deterministic behavior under strict budgets

3. Incremental, testable memory updates

4. Modular design for LLM API integration

### Example Use Cases

1. Chat-based AI assistants

2. Agentic AI systems with long task histories

3. Retrieval-augmented generation pipelines

4. Multi-turn decision support systems

### Tech Stack

1. Python

2. Model-specific tokenization utilities

3. Modular memory management components

### Learning Outcome

This project demonstrates how classic algorithmic techniques can be applied to real-world AI system design, bridging interview-style problem solving with production constraints.
