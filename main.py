def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(chars_dict)
    chars_dict_list = convert_dict_to_list(chars_dict)
    # print(chars_dict_list)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document", "\n")

    for dict in chars_dict_list:
        print(f"The '{dict["name"]}' character was found {dict["num"]} times") if dict["name"].isalpha() else next

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    chars_dict_list = []
    
    for char, val in dict.items():
        chars_dict_list.append({"name" : char, "num" : val})

    chars_dict_list.sort(reverse=True, key=sort_on)

    return chars_dict_list

main()