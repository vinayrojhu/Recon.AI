import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class LocalSentenceMatcher:

    def __init__(self, sentence_dict, file_mapping):

        self.sentence_dict = sentence_dict
        self.file_mapping = file_mapping

        self.codes = list(sentence_dict.keys())
        self.original_texts = list(sentence_dict.values())

        self.normalized_texts = [
            self.normalize_predefined_sentence(text)
            for text in self.original_texts
        ]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )

        self.matrix = self.vectorizer.fit_transform(self.normalized_texts)

    def clean_text(self, text):

        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def normalize_predefined_sentence(self, text):

        text = self.clean_text(text)

        # Replace standalone A/B/C placeholders with FILE_REF
        for placeholder in self.file_mapping.keys():
            text = re.sub(
                rf"\b{placeholder.lower()}\b",
                "file_ref",
                text
            )

        text = self.remove_filler_words(text)

        return text

    def normalize_user_sentence(self, text):

        text = self.clean_text(text)

        # Replace actual file names entered by user with FILE_REF
        for file_name in self.file_mapping.values():

            clean_file_name = self.clean_text(file_name)

            if clean_file_name:
                text = re.sub(
                    rf"\b{re.escape(clean_file_name)}\b",
                    "file_ref",
                    text
                )

        text = self.remove_filler_words(text)

        return text

    def remove_filler_words(self, text):

        filler_words = {
            "the",
            "as",
            "was",
            "is",
            "are",
            "a",
            "an",
            "to",
            "be",
            "set"
        }

        words = [
            word
            for word in text.split()
            if word not in filler_words
        ]

        return " ".join(words)

    def detect_files_in_user_sentence(self, user_sentence):

        detected_files = []

        clean_user_sentence = self.clean_text(user_sentence)

        for placeholder, file_name in self.file_mapping.items():

            clean_file_name = self.clean_text(file_name)

            if clean_file_name and clean_file_name in clean_user_sentence:
                detected_files.append({
                    "placeholder": placeholder,
                    "file_name": file_name
                })

        return detected_files

    def prepare_display_sentence(self, predefined_sentence, detected_files):

        display_sentence = predefined_sentence

        used_file_index = 0

        placeholders_found = re.findall(
            r"\b[A-Z]\b",
            display_sentence
        )

        for placeholder in placeholders_found:

            if used_file_index < len(detected_files):

                replacement_name = detected_files[used_file_index]["file_name"]
                used_file_index += 1

            else:

                replacement_name = self.file_mapping.get(
                    placeholder,
                    placeholder
                )

            display_sentence = re.sub(
                rf"\b{placeholder}\b",
                replacement_name,
                display_sentence,
                count=1
            )

        return display_sentence

    def get_top_matches(self, user_sentence, top_n=3):

        normalized_user_sentence = self.normalize_user_sentence(user_sentence)

        user_vector = self.vectorizer.transform([normalized_user_sentence])

        scores = cosine_similarity(user_vector, self.matrix)[0]

        detected_files = self.detect_files_in_user_sentence(user_sentence)

        ranked = sorted(
            zip(self.codes, self.original_texts, scores),
            key=lambda x: x[2],
            reverse=True
        )

        final_matches = []

        for code, original_sentence, score in ranked[:top_n]:

            display_sentence = self.prepare_display_sentence(
                original_sentence,
                detected_files
            )

            final_matches.append(
                (
                    code,
                    original_sentence,
                    display_sentence,
                    score
                )
            )

        return final_matches

    def get_file_mapping():

        file_mapping = {}

        while True:

            try:
                file_count = int(
                    input("How many files do you want to enter? : ")
                )

                if file_count > 0:
                    break

                print("Please enter a number greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        for i in range(file_count):

            placeholder = chr(65 + i)

            file_mapping[placeholder] = input(
                f"Enter File {placeholder} Name : "
            ).strip()

        return file_mapping

    def swap_placeholders(text, ph1, ph2):

        temp = "__TEMP__"

        text = text.replace(ph1, temp)
        text = text.replace(ph2, ph1)
        text = text.replace(temp, ph2)

        return text


    def rotate_file_mapping(file_mapping):

        keys = list(file_mapping.keys())
        values = list(file_mapping.values())

        values = values[1:] + values[:1]

        return dict(zip(keys, values))


    def randomize_used_files(file_mapping, detected_files):

        new_mapping = file_mapping.copy()

        placeholders = [
            item["placeholder"]
            for item in detected_files
        ]

        values = [
            file_mapping[p]
            for p in placeholders
        ]

        random.shuffle(values)

        for placeholder, value in zip(placeholders, values):
            new_mapping[placeholder] = value

        return new_mapping