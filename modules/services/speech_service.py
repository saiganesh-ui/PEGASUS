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

        result = self.model.transcribe(
            audio_path,
            language="en",
            task="transcribe",
            fp16=False,
            temperature=0,
            condition_on_previous_text=False,
            no_speech_threshold=0.6,
            logprob_threshold=-1.0,
            compression_ratio_threshold=2.4,
            initial_prompt="Kruger, open Chrome, open Calculator, open Notepad."
        )

        text = result["text"].strip()

        return text