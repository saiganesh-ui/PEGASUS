"""
Microphone Service
Project PEGASUS
"""

import time

import numpy as np
import sounddevice as sd
import soundfile as sf


class MicrophoneService:

    def __init__(self):

        self.samplerate = 16000
        self.channels = 1

        # Based on actual microphone measurements
        self.threshold = 0.05

        # Maximum time waiting for speech
        self.max_wait = 8

        # Silence required to finish command
        self.silence_duration = 0.8

        # Maximum command duration
        self.max_recording = 8

        # 100 ms chunks
        self.chunk_size = 1600

    def _rms(self, audio):

        audio = np.asarray(
            audio,
            dtype=np.float32
        )

        return float(
            np.sqrt(
                np.mean(
                    np.square(audio)
                )
            )
        )

    def record(
        self,
        filename="temp_recording.wav"
    ):

        print("🎤 Listening...")

        recorded = []

        speech_started = False

        silence_start = None

        wait_start = time.time()

        try:

            # -------------------------------------------------
            # KEEP ONE MICROPHONE STREAM OPEN
            # -------------------------------------------------

            with sd.InputStream(
                samplerate=self.samplerate,
                channels=self.channels,
                dtype="float32",
                blocksize=self.chunk_size
            ) as stream:

                while True:

                    chunk, overflowed = stream.read(
                        self.chunk_size
                    )

                    level = self._rms(chunk)

                    # -------------------------------------------------
                    # WAIT FOR SPEECH
                    # -------------------------------------------------

                    if not speech_started:

                        if level >= self.threshold:

                            speech_started = True

                            print(
                                f"🎙️ Speech detected "
                                f"(level: {level:.3f})"
                            )

                            recorded.append(
                                chunk.copy()
                            )

                            silence_start = None

                        elif (
                            time.time() - wait_start
                            >= self.max_wait
                        ):

                            print(
                                "⏱️ No speech detected."
                            )

                            return None

                        continue

                    # -------------------------------------------------
                    # SPEECH IS ACTIVE
                    # -------------------------------------------------

                    recorded.append(
                        chunk.copy()
                    )

                    if level >= self.threshold:

                        silence_start = None

                    else:

                        if silence_start is None:

                            silence_start = time.time()

                        elif (
                            time.time() - silence_start
                            >= self.silence_duration
                        ):

                            break

                    # -------------------------------------------------
                    # MAX RECORDING TIME
                    # -------------------------------------------------

                    duration = (
                        sum(
                            len(part)
                            for part in recorded
                        )
                        / self.samplerate
                    )

                    if duration >= self.max_recording:

                        break

        except Exception as e:

            print(
                f"🎤 Microphone error: {e}"
            )

            return None

        # -------------------------------------------------
        # NO AUDIO
        # -------------------------------------------------

        if not recorded:

            return None

        # -------------------------------------------------
        # COMBINE AUDIO
        # -------------------------------------------------

        audio = np.concatenate(
            recorded,
            axis=0
        )

        # -------------------------------------------------
        # SAVE
        # -------------------------------------------------

        sf.write(
            filename,
            audio,
            self.samplerate
        )

        print("🎙️ Recording complete.")

        return filename