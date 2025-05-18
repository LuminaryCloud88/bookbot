import sys
from stats import get_num, get_chars_dict, sort_on, sorted_dicts
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



def main():
    
    filepath = sys.argv[1]
    
    file_contents=get_book_text(filepath)
    num_words = get_num(file_contents)
    char_count = get_chars_dict(file_contents)
    alpha_sorted_char = sorted_dicts(char_count)
#    print(file_contents)
#    print(f"{num_words} words found in the document")
#    print(char_count)
#    print(alpha_sorted_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath} ...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in alpha_sorted_char:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
         return f.read()
    
main()