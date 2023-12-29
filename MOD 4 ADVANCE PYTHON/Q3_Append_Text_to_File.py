def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)

def append_and_display_text(file_path, new_text):
    with open(file_path, 'a') as file:
        file.write(new_text)

    read_entire_file(file_path)

append_and_display_text('example.txt', 'My Name is Son Goku.')