def read_file_into_variable(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content

# Example usage:
file_content = read_file_into_variable(r'C:\Users\name\Desktop\assignment modwise\MOD 4 ADVANCE PYTHON\examplefile.txt')
print(file_content)
