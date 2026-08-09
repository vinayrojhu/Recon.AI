import csv
import json
import os
from datetime import datetime


class LearningEngine:

    def __init__(self):

        
        BASE_DIR = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.learning_queue_file = os.path.join(
            BASE_DIR,
            "data",
            "learning_queue.csv"
        )
        self.feedback_file = os.path.join(
            BASE_DIR,
            "data",
            "feedback.csv"
        )
        self.stats_file = os.path.join(
            BASE_DIR,
            "data",
            "command_stats.json"
        )


        # self.learning_queue_file = "data/learning_queue.csv"
        # self.feedback_file = "data/feedback.csv"
        # self.stats_file = "data/command_stats.json"

    # =====================================================
    # LEARNING QUEUE
    # =====================================================

    def save_unmatched_sentence(
        self,
        user_sentence,
        matches,
        entities
    ):

        os.makedirs("data", exist_ok=True)

        file_exists = os.path.exists(
            self.learning_queue_file
        )

        with open(
            self.learning_queue_file,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            if not file_exists:

                writer.writerow([
                    "timestamp",
                    "user_sentence",
                    "top_match_1",
                    "top_match_2",
                    "top_match_3",
                    "entities"
                ])

            top1 = matches[0][0] if len(matches) > 0 else ""
            top2 = matches[1][0] if len(matches) > 1 else ""
            top3 = matches[2][0] if len(matches) > 2 else ""

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_sentence,
                top1,
                top2,
                top3,
                json.dumps(entities)
            ])

        print(
            "\nSentence added to learning queue."
        )

        print(
            "\nLearning Queue File :",
            os.path.abspath(self.learning_queue_file)
        )

    # =====================================================
    # FEEDBACK
    # =====================================================

    def save_feedback(
        self,
        command_code,
        result
    ):

        os.makedirs("data", exist_ok=True)

        file_exists = os.path.exists(
            self.feedback_file
        )

        with open(
            self.feedback_file,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            if not file_exists:

                writer.writerow([
                    "timestamp",
                    "command_code",
                    "result"
                ])

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                command_code,
                result
            ])

        self.update_command_stats(
            command_code,
            result
        )

    # =====================================================
    # COMMAND STATS
    # =====================================================

    def update_command_stats(
        self,
        command_code,
        result
    ):

        stats = {}

        if os.path.exists(
            self.stats_file
        ):

            with open(
                self.stats_file,
                "r",
                encoding="utf-8"
            ) as f:

                stats = json.load(f)

        if command_code not in stats:

            stats[command_code] = {
                "total": 0,
                "correct": 0,
                "incorrect": 0,
                "accuracy": 0
            }

        stats[command_code]["total"] += 1

        if result.upper() == "Y":

            stats[command_code]["correct"] += 1

        else:

            stats[command_code]["incorrect"] += 1

        total = stats[command_code]["total"]

        stats[command_code]["accuracy"] = round(
            stats[command_code]["correct"] / total,
            4
        )

        with open(
            self.stats_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                stats,
                f,
                indent=4
            )