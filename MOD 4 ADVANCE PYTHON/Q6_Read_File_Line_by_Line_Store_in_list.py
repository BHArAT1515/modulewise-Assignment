def read_file_into_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")

# Example usage:
lines_list = read_file_into_list('example.txt')
if lines_list:
    print(lines_list)
