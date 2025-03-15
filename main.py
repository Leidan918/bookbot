from stats import count_words

def get_book_text(book):
    with open(f"./books/{book}") as f:
        file_contents = f.read()
        return file_contents

def main():
    content_str = get_book_text(
        "frankenstein.txt"
    )
    word_count = count_words(content_str)
    print(f"{word_count} words found in the document")

main()