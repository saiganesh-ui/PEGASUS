"""
Voice Service
Project PEGASUS
"""

import pyttsx3
from modules.services.voice_settings import VoiceSettings

class VoiceService:

    def __init__(self):

        self.settings = VoiceSettings()

    def speak(self, text):

        if not self.settings.enabled:
            return

        print(f"[VOICE] {text}")

        engine = pyttsx3.init()

        engine.setProperty("rate", self.settings.rate)

        engine.setProperty("volume", self.settings.volume)

        voices = engine.getProperty("voices")

        if voices:

            index = min(
                self.settings.voice_index,
                len(voices) - 1
            )

            engine.setProperty(
                "voice",
                voices[index].id
            )

        engine.say(text)

        engine.runAndWait()

        engine.stop()