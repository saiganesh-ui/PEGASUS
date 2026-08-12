from modules.brain.qwen_service import QwenService

qwen = QwenService()

while True:
    text = input("You: ")

    if text.lower() in ["exit", "quit"]:
        break

    reply = qwen.ask(text)

    print()
    print("KRUGER:", reply)
    print()