from modules.services.wake_word_service import WakeWordService

wake = WakeWordService()

print(wake.process("KRUGER open chrome"))

print(wake.process("Krugar tell me the time"))

print(wake.process("Good morning"))