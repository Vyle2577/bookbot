import sys
from stats import num_words, char_count, get_sorted_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) >= 2:
        text = get_book_text(sys.argv[1])
        count = num_words(text)
        char_counts = char_count(text)
        sorted_char = get_sorted_list(char_counts)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {sys.argv[1]}...')
        print('----------- Word Count ----------')
        print(f'Found {count} total words')
        print('--------- Character Count -------')
        for item in sorted_char:
            print(f"{item['char']}: {item['num']}")
        print('============= END ===============')
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

main()