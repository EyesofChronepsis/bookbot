import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    # getting text from book
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # getting word count from the text
    from stats import word_count
    num_words = word_count(text)

    # getting the characters and counts 
    from stats import characters
    character_count = characters(text)

    # sorting the chracters
    from stats import report
    report_output = report(character_count)
   
    # print code 
    report_compile = ("============ BOOKBOT ============\n"
                     f"Analyzing book found at {sys.argv[1]}...)\n"
                      "----------- Word Count ----------\n"
                     f"Found {num_words} total words\n"
                      "--------- Character Count -------"
                     )

    list_length = len(report_output)
    print(report_compile)
    for i in range(list_length):
        print(f"{report_output[i]['char']}: {report_output[i]['num']}")

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents

main()