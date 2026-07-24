"""
Text Normalizer
Project PEGASUS
"""

import string


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
        "kindly",
        "to",
        "the",
        "a",
        "an"
    }

    def normalize(self, text):

        text = text.lower()

        # Remove punctuation
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        words = []

        for word in text.split():

            if word not in self.FILLER_WORDS:

                words.append(word)

        return " ".join(words)