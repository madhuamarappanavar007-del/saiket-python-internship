FILE_NAME = "sample.txt"


def read_file():
    """Read and return the contents of the sample file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' was not found.")
    except OSError as error:
        print(f"Error while reading the file: {error}")

    return None


def write_file(content):
    """Write the modified content to the sample file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write(content)
        return True
    except OSError as error:
        print(f"Error while saving the file: {error}")
        return False


def main():
    content = read_file()

    if content is None:
        return

    print("===== BASIC FILE HANDLING =====")
    print("\nOriginal content:")
    print(content)

    find_word = input("\nEnter the word to find: ").strip()
    if not find_word:
        print("Find word cannot be empty.")
        return

    replace_word = input("Enter the replacement word: ").strip()
    if not replace_word:
        print("Replacement word cannot be empty.")
        return

    if find_word not in content:
        print(f"The word '{find_word}' was not found in the file.")
        return

    modified_content = content.replace(find_word, replace_word)

    if write_file(modified_content):
        print("\nFile updated successfully.")
        print("\nModified content:")
        print(modified_content)


if __name__ == "__main__":
    main()
