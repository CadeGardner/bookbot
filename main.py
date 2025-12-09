import sys
from stats import get_word_count, get_letter_usage, format_dictionary

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
def print_header(file_path):
    print("============ BOOKBOT ============\n")
    print(f'Analyzing book found at {file_path}...\n')
    
def print_word_count(text):
    print("----------- Word Count ----------\n")
    get_word_count(text)

def print_character_count(list_of_letter_counts):
    print("\n--------- Character Count -------\n")
    for item in list_of_letter_counts:
         if(not item["char"].isalpha()): continue
         print(f'{item["char"]}: {item["num"]}\n')
    print("============= END ===============")

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    letter_counts = get_letter_usage(text)
    formatted_list_of_letters = format_dictionary(letter_counts)
    
    print_header(file_path)
    print_word_count(text)
    print_character_count(formatted_list_of_letters)


main()

