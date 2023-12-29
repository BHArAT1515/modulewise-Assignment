"""def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")

# Example usage:
file_path = 'examplefile.txt'  # Replace with the path to your file
read_file(file_path)
"""



def read_file_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error : file '{file_path} not found.")
    except UnicodeDecodeError as e:
        print(f"Error decoding the file : {e}")
        
file_path = 'examplefile.txt'
read_file_text(file_path)