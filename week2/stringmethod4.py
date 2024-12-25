# Example of various string methods

def string_methods():
    s = "   hello world   "

    # capitalize() example
    capitalized = s.capitalize()
    print(f"capitalize(): {capitalized}")  # Output: "Hello world"

    # title() example
    title_case = s.title()
    print(f"title(): {title_case}")  # Output: "Hello World"

    # center() example
    centered = s.center(20)
    print(f"center(20): '{centered}'")  # Output: "   hello world    "

    # count(sub) example
    count_occurrences = s.count('o')
    print(f"count('o'): {count_occurrences}")  # Output: 2

    # find(sub) example
    find_position = s.find('o')
    print(f"find('o'): {find_position}")  # Output: 4

    # join(list) example
    words = ["apple", "banana", "cherry"]
    joined_string = ", ".join(words)
    print(f"join(list): '{joined_string}'")  # Output: "apple, banana, cherry"

    # ljust(width) example
    left_justified = s.ljust(20)
    print(f"ljust(20): '{left_justified}'")  # Output: "   hello world       "

    # lower() example
    lower_case = s.lower()
    print(f"lower(): '{lower_case}'")  # Output: "   hello world   "

    # lstrip() example
    stripped_left = s.lstrip()
    print(f"lstrip(): '{stripped_left}'")  # Output: "hello world   "

    # replace(oldsub, newsub) example
    replaced = s.replace('hello', 'hi')
    print(f"replace('hello', 'hi'): '{replaced}'")  # Output: "   hi world   "

    # rfind(sub) example
    right_find_position = s.rfind('o')
    print(f"rfind('o'): {right_find_position}")  # Output: 10

    # rjust(width) example
    right_justified = s.rjust(20)
    print(f"rjust(20): '{right_justified}'")  # Output: "       hello world   "

    # rstrip() example
    stripped_right = s.rstrip()
    print(f"rstrip(): '{stripped_right}'")  # Output: "   hello world"

    # split() example
    splitted = s.split()
    print(f"split(): {splitted}")  # Output: ['hello', 'world']

    # upper() example
    upper_case = s.upper()
    print(f"upper(): '{upper_case}'")  # Output: "   HELLO WORLD   "

string_methods()