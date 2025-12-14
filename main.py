from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")
    print(count_letters(book_text))

main()
