def main():
    book_path = "book/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_word_count = get_book_word_count(book_text)
    book_char_count = get_char_count_dict(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_word_count} found in the document")

    # calling .items on a dict returns a tuple of key/value. eq. ("a": 1)
    book_char_count_list = list(book_char_count.items())
    # .sort is a mutable sort
    book_char_count_list.sort(reverse=True, key=get_char_count)

    for char, count in book_char_count_list:
        # Checks if the string is a character from the alphabet
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def get_char_count(char_count_pair):
    return char_count_pair[1]


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_book_word_count(text):
    words = text.split()
    return len(words)


def get_char_count_dict(text):
    char_dict = {}
    for char in text:
        key = char.lower()
        if key in char_dict.keys():
            char_dict[key] += 1
        else:
            char_dict[key] = 1
    return char_dict


main()