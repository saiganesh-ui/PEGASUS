from modules.services.speech_service import SpeechService

speech = SpeechService()

text = speech.listen()

print(text)

