import re
import random
from core.learning_engine import LearningEngine


class CommandSelector:

    def __init__(self):
        
        self.learning_engine = LearningEngine()

    # ==========================================================
    # DISPLAY TOP MATCHES
    # ==========================================================

    def display_matches(self, matches):

        print("\nTop Matches:")
        print("-" * 70)

        for idx, (code, original_sentence, display_sentence, score) in enumerate(matches, start=1):

            print(f"{idx}. {code}")
            print(f"   Original : {original_sentence}")
            print(f"   Display  : {display_sentence}")
            print(f"   Score    : {score:.4f}")
            print()

    # ==========================================================
    # MAIN COMMAND SELECTION
    # ==========================================================

    def choose_command(self, matches, matcher, file_mapping, user_input):

        if not matches:
            print("No matches found.")
            return None

        enhanced_matches = []

        for code, original_sentence, display_sentence, score in matches:

            preview_mapping = self.build_preview_mapping(
                original_sentence=original_sentence,
                file_mapping=file_mapping,
                matcher=matcher,
                user_input=user_input
            )

            entities = self.extract_entities(
                matcher=matcher,
                file_mapping=file_mapping,
                final_mapping=preview_mapping,
                user_input=user_input
            )

            display_sentence = self.replace_placeholders(
                original_sentence,
                preview_mapping
            )

            display_sentence = self.replace_columns_and_keys(
                display_sentence,
                entities
            )

            enhanced_matches.append(
                (
                    code,
                    original_sentence,
                    display_sentence,
                    score
                )
            )

        self.display_matches(enhanced_matches)

        matches = enhanced_matches

        while True:

            choice = input(
                f"Select a match (1-{len(matches)}) or 0 to cancel: "
            ).strip()

            if not choice.isdigit():
                print("Invalid selection.")
                continue

            choice = int(choice)

            if choice == 0:

                entities = self.extract_entities(
                    matcher=matcher,
                    file_mapping=file_mapping,
                    final_mapping=file_mapping,
                    user_input=user_input
                )

                save_choice = input(
                    "\nSave this sentence to Learning Queue? (Y/N): "
                ).strip().upper()

                if save_choice == "Y":

                    self.learning_engine.save_unmatched_sentence(
                        user_sentence=user_input,
                        matches=matches,
                        entities=entities
                    )

                print("Operation cancelled.")

                return None

            if 1 <= choice <= len(matches):

                selected = matches[choice - 1]

                code = selected[0]
                original_sentence = selected[1]
                score = selected[3]

                final_sentence, final_mapping = self.handle_file_reassignment(
                    original_sentence=original_sentence,
                    matcher=matcher,
                    file_mapping=file_mapping,
                    user_input=user_input
                )

                entities = self.extract_entities(
                    matcher=matcher,
                    file_mapping=file_mapping,
                    final_mapping=final_mapping,
                    user_input=user_input
                )

                result = {
                    "code": code,
                    "original_sentence": original_sentence,
                    "final_sentence": final_sentence,
                    "score": score,
                    "final_mapping": final_mapping,
                    "entities": entities
                }

                print("\nFinal Selection:")
                print("-" * 40)
                print(f"Code              : {result['code']}")
                print(f"Original Sentence : {result['original_sentence']}")
                print(f"Final Sentence    : {result['final_sentence']}")
                print(f"Score             : {result['score']}")
                print("-" * 40)

                self.print_final_mapping(final_mapping)
                self.print_entities(entities)

                feedback = input(
                    "\nWas this command correct? (Y/N): "
                ).strip().upper()

                if feedback not in ["Y", "N"]:
                    feedback = "N"

                self.learning_engine.save_feedback(
                    command_code=code,
                    result=feedback
                )

                return result

            print("Invalid selection.")

    # ==========================================================
    # PREVIEW MAPPING FOR TOP 3 OPTIONS
    # ==========================================================

    def build_preview_mapping(
        self,
        original_sentence,
        file_mapping,
        matcher,
        user_input
    ):

        detected_files = self.get_detected_files_in_user_order(
            matcher=matcher,
            file_mapping=file_mapping,
            user_input=user_input
        )

        preview_mapping = self.build_sentence_level_mapping(
            original_sentence=original_sentence,
            file_mapping=file_mapping,
            detected_files=detected_files
        )

        return preview_mapping

    # ==========================================================
    # FILE REASSIGNMENT / SHUFFLE LOGIC
    # ==========================================================

    def handle_file_reassignment(
        self,
        original_sentence,
        matcher,
        file_mapping,
        user_input
    ):

        detected_files = self.get_detected_files_in_user_order(
            matcher=matcher,
            file_mapping=file_mapping,
            user_input=user_input
        )

        placeholders_in_sentence = self.get_placeholders_from_sentence(
            original_sentence
        )

        current_mapping = self.build_sentence_level_mapping(
            original_sentence=original_sentence,
            file_mapping=file_mapping,
            detected_files=detected_files
        )

        display_sentence = self.build_final_display_sentence(
            original_sentence=original_sentence,
            matcher=matcher,
            file_mapping=file_mapping,
            current_mapping=current_mapping,
            user_input=user_input
        )

        if len(detected_files) > 1:

            while True:

                print("\nCurrent Sentence:")
                print(display_sentence)

                shuffle_choice = input(
                    "\nRandomly reassign mentioned files? (Y/N): "
                ).strip().upper()

                if shuffle_choice != "Y":
                    break

                used_placeholders = placeholders_in_sentence[:len(detected_files)]

                current_mapping = self.randomize_only_detected_files(
                    current_mapping=current_mapping,
                    placeholders=used_placeholders,
                    detected_files=detected_files
                )

                display_sentence = self.build_final_display_sentence(
                    original_sentence=original_sentence,
                    matcher=matcher,
                    file_mapping=file_mapping,
                    current_mapping=current_mapping,
                    user_input=user_input
                )

        return display_sentence, current_mapping

    def build_final_display_sentence(
        self,
        original_sentence,
        matcher,
        file_mapping,
        current_mapping,
        user_input
    ):

        display_sentence = self.replace_placeholders(
            original_sentence,
            current_mapping
        )

        entities = self.extract_entities(
            matcher=matcher,
            file_mapping=file_mapping,
            final_mapping=current_mapping,
            user_input=user_input
        )

        display_sentence = self.replace_columns_and_keys(
            display_sentence,
            entities
        )

        return display_sentence

    # ==========================================================
    # PLACEHOLDER / FILE MAPPING HELPERS
    # ==========================================================

    def get_placeholders_from_sentence(self, sentence):

        placeholders = re.findall(
            r"\b[A-Z]\b",
            sentence
        )

        unique_placeholders = []

        for ph in placeholders:
            if ph not in unique_placeholders:
                unique_placeholders.append(ph)

        return unique_placeholders

    def get_detected_files_in_user_order(
        self,
        matcher,
        file_mapping,
        user_input
    ):

        detected = []

        clean_user_input = matcher.clean_text(user_input)

        for placeholder, file_name in file_mapping.items():

            clean_file_name = matcher.clean_text(file_name)

            if not clean_file_name:
                continue

            position = clean_user_input.find(clean_file_name)

            if position != -1:
                detected.append(
                    {
                        "placeholder": placeholder,
                        "file_name": file_name,
                        "position": position
                    }
                )

        detected.sort(
            key=lambda x: x["position"]
        )

        return detected

    def build_sentence_level_mapping(
        self,
        original_sentence,
        file_mapping,
        detected_files
    ):

        current_mapping = file_mapping.copy()

        placeholders_in_sentence = self.get_placeholders_from_sentence(
            original_sentence
        )

        for index, target_placeholder in enumerate(placeholders_in_sentence):

            if index >= len(detected_files):
                break

            detected_file_name = detected_files[index]["file_name"]

            source_placeholder = None

            for ph, existing_file_name in current_mapping.items():

                if existing_file_name.lower() == detected_file_name.lower():
                    source_placeholder = ph
                    break

            if source_placeholder and source_placeholder != target_placeholder:

                temp_value = current_mapping[target_placeholder]

                current_mapping[target_placeholder] = detected_file_name

                current_mapping[source_placeholder] = temp_value

            elif not source_placeholder:

                current_mapping[target_placeholder] = detected_file_name

        return current_mapping

    def randomize_only_detected_files(
        self,
        current_mapping,
        placeholders,
        detected_files
    ):

        new_mapping = current_mapping.copy()

        target_placeholders = placeholders[:len(detected_files)]

        if len(target_placeholders) < 2:
            return new_mapping

        old_values = [
            new_mapping[ph]
            for ph in target_placeholders
        ]

        new_values = old_values.copy()

        while new_values == old_values:
            random.shuffle(new_values)

        for placeholder, file_name in zip(target_placeholders, new_values):
            new_mapping[placeholder] = file_name

        return new_mapping

    def replace_placeholders(
        self,
        sentence,
        mapping
    ):

        display_sentence = sentence

        for placeholder, file_name in mapping.items():

            display_sentence = re.sub(
                rf"\b{placeholder}\b",
                file_name,
                display_sentence
            )

        return display_sentence

    # ==========================================================
    # ENTITY EXTRACTION LOGIC
    # ==========================================================

    def extract_entities(
        self,
        matcher,
        file_mapping,
        final_mapping,
        user_input
    ):

        clean_input = matcher.clean_text(user_input)

        detected_files = self.get_detected_files_with_positions(
            matcher=matcher,
            file_mapping=file_mapping,
            final_mapping=final_mapping,
            user_input=user_input
        )

        column_mentions = self.detect_column_mentions(
            clean_input
        )

        match_keys = self.detect_match_keys(
            clean_input
        )

        entities = {
            "files": [],
            "match_keys": match_keys
        }

        for file_item in detected_files:

            entities["files"].append(
                {
                    "placeholder": file_item["placeholder"],
                    "file_name": file_item["file_name"],
                    "columns": []
                }
            )

        for column_item in column_mentions:

            if column_item["name"].lower() in [k.lower() for k in match_keys]:
                continue

            nearest_file = self.find_nearest_file(
                column_item=column_item,
                detected_files=detected_files
            )

            if nearest_file is None:
                continue

            for file_entity in entities["files"]:

                if (
                    file_entity["file_name"].lower()
                    == nearest_file["file_name"].lower()
                ):

                    if column_item["name"] not in file_entity["columns"]:
                        file_entity["columns"].append(
                            column_item["name"]
                        )

                    break

        return entities

    def get_detected_files_with_positions(
        self,
        matcher,
        file_mapping,
        final_mapping,
        user_input
    ):

        detected = []

        clean_user_input = matcher.clean_text(user_input)

        for original_placeholder, file_name in file_mapping.items():

            clean_file_name = matcher.clean_text(file_name)

            if not clean_file_name:
                continue

            position = clean_user_input.find(clean_file_name)

            if position == -1:
                continue

            final_placeholder = self.find_placeholder_by_file_name(
                final_mapping,
                file_name
            )

            detected.append(
                {
                    "placeholder": final_placeholder,
                    "file_name": file_name,
                    "position": position,
                    "end_position": position + len(clean_file_name)
                }
            )

        detected.sort(
            key=lambda x: x["position"]
        )

        # print("\nDEBUG DETECTED FILES")
        # for item in detected:
        #     print(item)

        return detected

    def find_placeholder_by_file_name(
        self,
        final_mapping,
        file_name
    ):

        for placeholder, mapped_file_name in final_mapping.items():

            if mapped_file_name.lower() == file_name.lower():
                return placeholder

        return None

    def detect_column_mentions(self, clean_input):

        column_mentions = []

        explicit_column_pattern = r"\b(?:column|col)\s+([a-z]{1,3}|[0-9]+|[a-z0-9_]+)\b"

        for match in re.finditer(explicit_column_pattern, clean_input):

            column_mentions.append(
                {
                    "name": match.group(1).strip().upper(),
                    "position": match.start(),
                    "end_position": match.end()
                }
            )

        business_field_patterns = [
            "quantity",
            "market value",
            "nav",
            "currency",
            "trade date",
            "settlement date",
            "isin",
            "account",
            "account number",
            "security code",
            "security name",
            "fund code",
            "amount",
            "balance",
            "price",
            "market price",
            "book value",
            "gl account",
            "broker code",
            "tolerance status"
        ]

        for field in business_field_patterns:

            pattern = rf"\b{re.escape(field)}\b"

            for match in re.finditer(pattern, clean_input):

                if self.is_probable_match_key(
                    clean_input,
                    match.start()
                ):
                    continue

                column_mentions.append(
                    {
                        "name": field,
                        "position": match.start(),
                        "end_position": match.end()
                    }
                )

        column_mentions = self.remove_duplicate_entities(
            column_mentions
        )

        column_mentions.sort(
            key=lambda x: x["position"]
        )

        return column_mentions

    def detect_match_keys(self, clean_input):

        keys = []

        patterns = [
            r"\bon\s+matching\s+([a-z0-9_ ]+)",
            r"\bmatching\s+([a-z0-9_ ]+)",
            r"\busing\s+([a-z0-9_ ]+)",
            r"\bon\s+([a-z0-9_ ]+)"
        ]

        stop_words = {
            "file",
            "column",
            "col",
            "with",
            "to",
            "from",
            "into",
            "where",
            "and",
            "or"
        }

        for pattern in patterns:

            match = re.search(pattern, clean_input)

            if not match:
                continue

            captured = match.group(1).strip()

            words = captured.split()

            key_words = []

            for word in words:

                if word in stop_words:
                    break

                key_words.append(word)

            if key_words:

                key = " ".join(key_words)

                if key not in keys:
                    keys.append(key)

        return keys

    def is_probable_match_key(
        self,
        clean_input,
        position
    ):

        before_text = clean_input[max(0, position - 25):position]

        key_indicators = [
            "matching",
            "on",
            "using"
        ]

        for indicator in key_indicators:

            if indicator in before_text.split():
                return True

        return False

    def find_nearest_file(
        self,
        column_item,
        detected_files
    ):

        if not detected_files:
            return None

        column_center = (
            column_item["position"]
            + column_item["end_position"]
        ) / 2

        nearest_file = None
        nearest_distance = None

        for file_item in detected_files:

            file_center = (
                file_item["position"]
                + file_item["end_position"]
            ) / 2

            distance = abs(column_center - file_center)

            if nearest_distance is None or distance < nearest_distance:
                nearest_distance = distance
                nearest_file = file_item

        return nearest_file

    def remove_duplicate_entities(
        self,
        entities
    ):

        unique = []
        seen = set()

        for item in entities:

            key = (
                item["name"],
                item["position"],
                item["end_position"]
            )

            if key not in seen:
                unique.append(item)
                seen.add(key)

        return unique

    # ==========================================================
    # COLUMN AND MATCH KEY REPLACEMENT LOGIC
    # ==========================================================

    def replace_columns_and_keys(
        self,
        sentence,
        entities
    ):

        updated_sentence = sentence

        files = entities.get("files", [])

        match_keys = entities.get("match_keys", [])

        if match_keys:

            key = match_keys[0].upper()

            updated_sentence = re.sub(
                r"\bmatching\s+column\s+1\b",
                f"matching {key}",
                updated_sentence,
                flags=re.IGNORECASE
            )

            updated_sentence = re.sub(
                r"\busing\s+column\s+1\b",
                f"using {key}",
                updated_sentence,
                flags=re.IGNORECASE
            )

            updated_sentence = re.sub(
                r"\bon\s+matching\s+column\s+1\b",
                f"on matching {key}",
                updated_sentence,
                flags=re.IGNORECASE
            )

        for file_item in files:

            file_name = file_item.get("file_name", "")
            columns = file_item.get("columns", [])

            if not file_name or not columns:
                continue

            file_name_pattern = re.escape(file_name)

            for column_value in columns:

                pattern = (
                    r"\bcolumn\s+([a-z0-9_]+)\b"
                    r"(?=(?:(?!\bfile\b).){0,80}\bfile\s+"
                    + file_name_pattern +
                    r"\b)"
                )

                updated_sentence = re.sub(
                    pattern,
                    f"column {column_value}",
                    updated_sentence,
                    count=1,
                    flags=re.IGNORECASE
                )

        return updated_sentence

    # ==========================================================
    # PRINTING HELPERS
    # ==========================================================

    def print_final_mapping(
        self,
        final_mapping
    ):

        print("\nFinal File Mapping:")
        print("-" * 40)

        for placeholder, file_name in sorted(final_mapping.items()):
            print(f"{placeholder} = {file_name}")

        print("-" * 40)

    def print_entities(
        self,
        entities
    ):

        print("\nDetected Entities:")
        print("-" * 40)

        files = entities.get("files", [])

        if files:

            print("Files:")

            for file_item in files:

                columns = file_item.get("columns", [])

                if columns:
                    column_text = ", ".join(columns)
                else:
                    column_text = ""

                print(
                    f"{file_item['placeholder']} = "
                    f"{file_item['file_name']} "
                    f"| Columns: {column_text}"
                )

        match_keys = entities.get("match_keys", [])

        if match_keys:

            print("\nMatch Keys:")

            for key in match_keys:
                print(f"- {key}")

        print("-" * 40)