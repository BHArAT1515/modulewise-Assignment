def find_longest_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        longest_words = max(words, key=len)
        return longest_words

# Example usage:
longest_words = find_longest_words('examplefile.txt')
print("Longest Words:", longest_words)
