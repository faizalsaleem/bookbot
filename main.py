from stats import get_num_words, get_num_chars, char_sort
from sys import argv

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    print("============ BOOKBOT ============")
    if len(argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
    file_path = argv[1]
    print(f'Analyzing book found at {file_path}')
    book_text = get_book_text(file_path)
    print('----------- Word Count ----------')
    count = get_num_words(book_text)
    print(f'Found {count} total words')
    print('----------- Character Count ----------')
    chars = get_num_chars(book_text)
    sorted_chars = char_sort(chars)
    for char, freq in sorted_chars:
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {freq}")
    print("============= END ===============")

main()