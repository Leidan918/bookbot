from stats import count_words, count_characters, sort_char
import sys

def get_book_text(book):
    with open(f"./{book}") as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content_str = get_book_text(
        sys.argv[1]
    )
    word_count = count_words(content_str)
    char_count = count_characters(content_str)
    sorted_char_count = sort_char(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sorted_char, val in sorted_char_count.items():
        if sorted_char.isalpha():
            print(f"{sorted_char}: {val}")
            continue
        else:
            continue
    print("============= END ===============")

main()