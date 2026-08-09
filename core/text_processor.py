import re


class TextProcessor:

    @staticmethod
    def clean_text(text):

        text = text.lower().strip()

        text = re.sub(
            r"[^a-z0-9\s]",
            " ",
            text
        )

        return re.sub(
            r"\s+",
            " ",
            text
        ).strip()

    @staticmethod
    def remove_filler_words(text):

        filler_words = {
            "the",
            "as",
            "is",
            "are",
            "a",
            "an",
            "to"
        }

        return " ".join(
            word
            for word in text.split()
            if word not in filler_words
        )