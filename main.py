FILE_PATH = 'notes.txt'


if __name__ == '__main__':
    all_lines = []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            all_lines.append(line)
            print(line)

    # reverse list
    all_lines = all_lines[::-1]

    new_file = '_'.join(['reversed', FILE_PATH])

    with open(new_file, 'w', encoding='utf-8') as file:
        for line in all_lines:
            file.write(line + '\n')

    print(f'\nSuccessfully reversed {FILE_PATH} and saved as {new_file}')
