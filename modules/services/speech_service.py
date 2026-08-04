"""
Speech Service
Project PEGASUS
"""

import whisper


class SpeechService:

    def __init__(self):

        print("Loading Whisper...")

        self.model = whisper.load_model("base")

        print("Whisper Ready.")

    def transcribe(self, audio_path):

        result = self.model.transcribe(audio_path)

        return result["text"].strip()