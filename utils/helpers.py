import random


def randomize_used_files(
    file_mapping,
    detected_files
):

    new_mapping = file_mapping.copy()

    placeholders = [
        x["placeholder"]
        for x in detected_files
    ]

    values = [
        file_mapping[p]
        for p in placeholders
    ]

    if len(values) > 1:

        old_values = values[:]

        while values == old_values:

            random.shuffle(values)

    for p, v in zip(placeholders, values):
        new_mapping[p] = v

    return new_mapping





