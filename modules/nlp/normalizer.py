"""
Text Normalizer
Project PEGASUS
"""


class Normalizer:

    FILLER_WORDS = {

        "please",
        "can",
        "could",
        "would",
        "will",
        "you",
        "me",
        "for",
        "kindly"

    }

    def normalize(self, text):

        text = text.lower().strip()

        words = []

        for word in text.split():

            if word not in self.FILLER_WORDS:

                words.append(word)

        return " ".join(words)