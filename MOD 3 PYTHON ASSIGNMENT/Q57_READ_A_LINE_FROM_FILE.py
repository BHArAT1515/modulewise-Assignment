import random

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            return None  # Return None if the file is empty

        random_line = random.choice(lines)
        return random_line.strip()  # Remove leading and trailing whitespaces

# Example usage:
file_path = 'assign.txt'  # Replace with the path to your file
random_line = read_random_line(file_path)

if random_line is not None:
    print("Random Line from the File:")
    print(random_line)
else:
    print("The file is empty.")
