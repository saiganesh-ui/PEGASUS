from modules.services.microphone_service import MicrophoneService
from modules.services.speech_service import SpeechService
from modules.services.wake_word_service import WakeWordService

mic = MicrophoneService()
speech = SpeechService()
wake = WakeWordService()

audio = mic.record()

text = speech.transcribe(audio)

print("Detected:", text)

result = wake.process(text)

print(result)