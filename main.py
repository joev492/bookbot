from stats import count_words, count_letters, dict_to_list
import sys
path = sys.argv[1]
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    book_text = get_book_text(path)
    sys.exit(1)

    letter_list = dict_to_list(count_letters(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
