def write_list_to_file(file_path, input_list):
    with open(file_path, 'w',) as file:
        for item in input_list:
            file.write(f"{item}\n")

# Example usage:
my_list = ["apple", "banana", "orange"]
write_list_to_file('output.txt', my_list)
