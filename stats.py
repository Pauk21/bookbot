def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def by_count(d):
    return d["num"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        dict_list.append(new_dict)
    dict_list.sort(key=by_count, reverse=True)
    return dict_list