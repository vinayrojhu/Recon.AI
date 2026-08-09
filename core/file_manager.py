def get_file_mapping():

    file_mapping = {}

    while True:

        try:

            file_count = int(
                input("How many files? : ")
            )

            if file_count > 0:
                break

        except ValueError:
            pass

    for i in range(file_count):

        placeholder = chr(65 + i)

        file_mapping[placeholder] = input(
            f"Enter File {placeholder} Name : "
        ).strip()

    return file_mapping