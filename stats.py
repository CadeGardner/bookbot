
def sort_descending(items):
    return items["num"]

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    print(f'Found {word_count} total words')

def get_letter_usage(text):
    letters = {}
    for item in text:
        char = item.lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters

def format_dictionary(clean_dictionary):
    formatted_word_counts = []

    for item in clean_dictionary:
        formatted_item = {"char": item, "num": clean_dictionary[item]}
        formatted_word_counts.append(formatted_item)
    
    formatted_word_counts.sort(reverse=True, key=sort_descending)
    return formatted_word_counts
    
