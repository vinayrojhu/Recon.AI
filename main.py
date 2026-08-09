from data.commands import SENTENCES

from core.file_manager import (
    get_file_mapping
)

from core.sentence_matcher import (
    LocalSentenceMatcher
)

from core.command_selector import (
    CommandSelector
)


def main():

    file_mapping = get_file_mapping()

    matcher = LocalSentenceMatcher(
        SENTENCES,
        file_mapping
    )

    selector = CommandSelector()

    while True:

        user_input = input(
            "\nEnter sentence: "
        ).strip()

        if user_input.lower() in [
            "exit",
            "quit"
        ]:
            break

        matches = matcher.get_top_matches(
            user_input
        )

        selector.choose_command(
            matches,
            matcher,
            file_mapping,
            user_input
        )


if __name__ == "__main__":
    main()