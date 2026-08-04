from modules.services.speech_service import SpeechService

speech = SpeechService()

text = speech.transcribe("tests/sample.m4a")

print(f"Detected: {text}")