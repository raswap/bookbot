import sys

from stats import get_char_count_dict, get_sorted_char_count, get_words_count


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_txt = get_book_text(book_path)
    num_words = get_words_count(book_txt)
    char_count = get_char_count_dict(book_txt)
    sorted_char_count = get_sorted_char_count(char_count)
    # print(sorted_char_count)
    # print(f"Found {num_words} total words")
    # print(sorted_char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
