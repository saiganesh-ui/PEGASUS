from modules.services.microphone_service import MicrophoneService
from modules.services.speech_service import SpeechService

mic = MicrophoneService()
speech = SpeechService()

audio = mic.record()

text = speech.transcribe(audio)

print("\nDetected:", text)