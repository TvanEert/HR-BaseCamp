def rec_print_folders(n: int, pref: str, root: list) -> None:
    structure = "Folder_0\n"
    layer = root
    point_folder = 0
    layer_number = 0
    pref = pref
    if type(layer[point_folder]) == list:
        layer_number += 1
        pref = ">"
        structure += pref * layer_number + "Folder_" + str(layer_number) + "\n"
        point_folder += 1

    elif type(layer[point_folder]) == str:
        pref = "-"
        structure += pref * layer_number + layer[point_folder] + "\n"
        point_folder += 1

    print(structure)


def rec_count_files(root: list, counter: int) -> int:
    counter = counter
    for file in root:
        if type(file) == str:
            counter += 1
        if type(file) == list:
            rec_count_files(file, counter)

    return counter


if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'], ['file_6', ['file_7', 'file_8'],
                                                              ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case, 0))