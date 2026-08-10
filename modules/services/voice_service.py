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

        if not text or not text.strip():
            return

        print(f"[VOICE] {text}")

        engine = None

        try:

            engine = pyttsx3.init("sapi5")

            engine.setProperty(
                "rate",
                self.settings.rate
            )

            engine.setProperty(
                "volume",
                self.settings.volume
            )

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

        except Exception as e:

            print(f"[VOICE ERROR] {e}")

        finally:

            if engine is not None:

                try:
                    engine.stop()
                except Exception:
                    pass

                del engine