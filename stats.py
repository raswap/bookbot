def get_words_count(text):
    return len(text.split())


def get_char_count_dict(text):
    char_count = {}
    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_on(items):
    return items["num"]


def get_sorted_char_count(char_count_dict):
    list_of_dict = [{"char": k, "num": v} for k, v in char_count_dict.items()]
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
