"""
KRUGER Voice Mode
Project PEGASUS
"""

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
print("Voice session active.")
print("Say 'Kruger, sleep' to deactivate.")
print("Say 'Kruger, exit' to shut down.")
print()


active = False


while True:

    try:

        audio = mic.record()

        if not audio:
            continue

        text = speech.transcribe(audio)

        if not text:
            continue

        print()
        print("Detected:", text)

        result = wake.process(text)

        # -------------------------------------------------
        # WAKE WORD DETECTED
        # -------------------------------------------------

        if result["wake"]:

            command = result["command"].strip()

            # Wake word alone
            if not command:

                active = True

                print("KRUGER: Voice session activated.")

                continue

            # -------------------------------------------------
            # EXIT
            # -------------------------------------------------

            if command in [
                "exit",
                "quit",
                "shutdown",
                "shut down"
            ]:

                print("KRUGER: Shutting down.")

                break

            # -------------------------------------------------
            # SLEEP
            # -------------------------------------------------

            if command in [
                "sleep",
                "go to sleep",
                "stand by",
                "standby"
            ]:

                active = False

                print("KRUGER: Voice session deactivated.")

                continue

            # Wake word + command automatically activates session
            active = True

        # -------------------------------------------------
        # IGNORE COMMAND IF SESSION IS NOT ACTIVE
        # -------------------------------------------------

        elif not active:

            continue

        else:

            command = result["command"].strip()

        # -------------------------------------------------
        # EMPTY COMMAND
        # -------------------------------------------------

        if not command:

            continue

        # -------------------------------------------------
        # EXECUTE
        # -------------------------------------------------

        response = engine.process(command)

        print()

        if isinstance(response, list):

            for item in response:

                print(item)

        else:

            print(response)

    except KeyboardInterrupt:

        print()
        print("KRUGER: Voice Mode stopped.")
        break