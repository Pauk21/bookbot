import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_dict


def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    book_word_count = get_word_count(book_text)
    book_character_count = get_character_count(book_text)
    sorted_characters = sort_dict(book_character_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print(f"--------- Character Count -------")
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")


main()