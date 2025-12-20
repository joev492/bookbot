from stats import count_words, count_letters, dict_to_list
import sys
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]   
    book_text = get_book_text(file_path)

    letter_list = dict_to_list(count_letters(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
