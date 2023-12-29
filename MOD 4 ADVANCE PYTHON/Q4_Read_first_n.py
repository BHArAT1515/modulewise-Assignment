def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()[:n]
            for line in lines:
                print(line.strip())
    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")

read_first_n_lines('examplefile.txt', 3)