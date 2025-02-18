with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def print_content():
    print(file_contents)

def count_word(contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_character(contents):
    character_count = {}
    contents = contents.lower()
    for char in contents:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def report_char(contents):
    character_count = count_character(contents)
    dict_list = []
    for char in character_count:
        if char.isalpha():
            dict_list.append({"char":char,"num":character_count[char]})
    dict_list.sort(reverse=True,key=sort_on)
    for char in dict_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")


def main():
    report_char(file_contents)

main()