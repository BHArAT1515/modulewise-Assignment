from collections import Counter

def count_word_frequency(file_path):
    with open(file_path, 'r', encoding = 'utf8') as file:
        words = file.read().split()
        word_frequency = Counter(words)
        return word_frequency

# Example usage:
word_frequency = count_word_frequency('examplefile.txt')
print("Word Frequency:", word_frequency)
