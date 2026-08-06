from core.engine import Engine

from modules.services.microphone_service import MicrophoneService
from modules.services.speech_service import SpeechService
from modules.services.wake_word_service import WakeWordService


engine = Engine()

mic = MicrophoneService()

speech = SpeechService()

wake = WakeWordService()


print()

print("K R U G E R")

print("Voice Mode Online")

print()

while True:

    audio = mic.record()

    text = speech.transcribe(audio)

    print()

    print("Detected:", text)

    result = wake.process(text)

    if not result["wake"]:

        continue

    response = engine.process(result["command"])

    if isinstance(response, list):

        for item in response:

            print(item)

    else:

        print(response)