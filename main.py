def main(): 
    book_path ='/home/bruceescott/workspace/github.com/bruceescott17/bookbot/books/Frankenstein.txt'
    file_contents = get_book_text(book_path)
    book_path_list = book_path.split("/")
    book_name = book_path_list[len(book_path_list) - 1]
    print(f"-- Begin report of {book_name} --")
    print(f"There are {word_count(file_contents)} words in the document.")
    print("")
    char_dict = get_chars_dict(file_contents)
    sort_alpha(get_dict_list(char_dict))
    print("-- End of Report --")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
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

def get_keys(dict):
    return dict.keys()
             

def get_dict_list(dict):
    dict_list = []
    keys = dict.keys()
    for key in keys:
        if key.isalpha() == True:
            char_dict = {}
            char_dict["letter"] = key
            char_dict["num"] = dict[key]
            dict_list.append(char_dict)
    return dict_list

def sort_on(dict):
    return dict["num"]

def sort_alpha(alpha_list):
    alpha_list.sort(reverse = True, key=sort_on)
    for a in alpha_list:
        print(f"The {a["letter"]} character was found {a["num"]} times")
    








if __name__ == "__main__":
    main()