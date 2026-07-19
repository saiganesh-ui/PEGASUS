"""
Text Normalizer
Project PEGASUS
"""


class Normalizer:

    def clean(self, text):

        text = text.lower()

        text = text.strip()

        return text