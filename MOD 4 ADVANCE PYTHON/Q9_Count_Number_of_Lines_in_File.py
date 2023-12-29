def count_lines(file_path):
    with open(file_path, 'r', encoding = 'utf8') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
line_count = count_lines('examplefile.txt')
print("Number of Lines:", line_count)
