import string
from collections import Counter


FILE_NAME = "sample.txt"
NUMBER_OF_COMMON_WORDS = 5


def read_file():
    """Read and return the original contents of the sample file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' was not found.")
    except OSError as error:
        print(f"Error while reading the file: {error}")

    return None


def clean_and_split_text(content):
    """Convert text to lowercase, remove punctuation, and split into words."""
    cleaned_text = content.lower()

    for punctuation_mark in string.punctuation:
        cleaned_text = cleaned_text.replace(punctuation_mark, " ")

    return cleaned_text.split()


def analyze_text(content):
    """Calculate lines, words, characters, and common-word frequencies."""
    lines = content.splitlines()
    words = clean_and_split_text(content)
    character_count = len(content)
    word_frequencies = Counter(words)
    common_words = word_frequencies.most_common(NUMBER_OF_COMMON_WORDS)

    return len(lines), len(words), character_count, common_words


def main():
    content = read_file()

    if content is None:
        return

    line_count, word_count, character_count, common_words = analyze_text(content)

    print("===== WORD COUNT TOOL =====")
    print(f"File: {FILE_NAME}")
    print("\nAnalysis results:")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")

    if not common_words:
        print("\nThe file is empty. No words were found.")
        return

    print("\nMost common words:")
    for number, (word, frequency) in enumerate(common_words, start=1):
        print(f"{number}. {word}: {frequency}")


if __name__ == "__main__":
    main()
