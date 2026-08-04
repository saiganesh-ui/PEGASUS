"""
Voice Settings
Project PEGASUS
"""


class VoiceSettings:

    def __init__(self):

        self.enabled = True

        self.rate = 175

        self.volume = 1.0

        self.voice_index = 0

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def set_rate(self, rate):

        self.rate = rate

    def set_volume(self, volume):

        self.volume = volume

    def set_voice(self, index):

        self.voice_index = index