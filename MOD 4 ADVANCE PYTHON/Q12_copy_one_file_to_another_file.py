def copy_file(source_file_path, destination_file_path):
    with open(source_file_path, 'r') as source_file:
        content = source_file.read()

    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(content)

# Example usage:
copy_file('example.txt', 'copy_example.txt')
