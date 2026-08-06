"""
Microphone Service
Project PEGASUS
"""

import sounddevice as sd
import soundfile as sf


class MicrophoneService:

    def record(self,
               filename="temp_recording.wav",
               duration=5,
               samplerate=16000):

        print("🎤 Listening...")

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(
            filename,
            audio,
            samplerate
        )

        return filename