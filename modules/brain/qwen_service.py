import subprocess

SYSTEM_PROMPT = (
    "You are KRUGER, a helpful personal AI assistant. "
    "Reply naturally, clearly, and briefly unless the user asks for details. "
    "If you are unsure about a fact, say you are not sure."
)

class QwenService:

    def __init__(self):
        self.history = []

    def ask(self, prompt: str) -> str:

        # Add user message to history
        self.history.append(f"User: {prompt}")

        # Build full conversation
        conversation = SYSTEM_PROMPT + "\n\n" + "\n".join(self.history) + "\nKRUGER:"

        result = subprocess.run(
            ["ollama", "run", "qwen2.5:3b", conversation],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        reply = result.stdout.strip()

        # Save assistant reply
        self.history.append(f"KRUGER: {reply}")

        return reply