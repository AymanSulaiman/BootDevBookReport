def count_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def main():
    try:
        with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        # Count words
        words = text.split()
        word_count = len(words)

        # Count characters
        char_count = count_characters(text)

        # Sort characters by count in descending order
        sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

        # Display results
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for char, count in sorted_chars:
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

if __name__ == "__main__":
    main()

