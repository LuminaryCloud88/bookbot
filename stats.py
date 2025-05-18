filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
         return f.read()
    
def get_num(file_contents):
    file_contents=get_book_text(filepath)
    num_words=file_contents.split()
    return len(num_words)

def get_chars_dict(file_contents):
    chars = {}
    file_contents_lowered = file_contents.lower()
    for c in file_contents_lowered:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(chars):
    return chars["num"]

def sorted_dicts(chars):
    char_list = [{ "char":char, "num": count} for char, count in chars.items() if char.isalpha()]
    sorted_char_list=sorted(char_list, reverse=True, key=sort_on)
    return sorted_char_list
