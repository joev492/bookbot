from operator import itemgetter
def count_words(book_text):
    count = 0
    for word in book_text.split():
        count += 1
    return count

def count_letters(book_text):
    #convert to lowercase and check if number
    letter_counts = {}
    for char in book_text:
        if char.isalpha():
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1
    return letter_counts

def sort_on(items):
    return items["num"]

def dict_to_list(book_dict):
    letter_list = []
    for key, value in book_dict.items():
        letter_dict = {"char": key,
                       "num" : value}
        letter_list.append(letter_dict)
    letter_list.sort(key=sort_on, reverse=True)
    return letter_list


