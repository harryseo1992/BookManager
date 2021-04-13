# Constant value
def SEARCH_CATEGORIES() -> list:
    """
    Create constant list of values for search categories.

    :return: A list of search categories defined by the text_file.
    # """
    library_tuple = get_info()
    return list(library_tuple[0].keys())


def SHELF_SET() -> set:  # Constant value
    """
    Create constant set of shelves.

    :return: A set of available shelves defined by the text_file.
    """
    library_tuple = get_info()
    return set(book_dictionary['Shelf'] for book_dictionary in library_tuple)


def get_info() -> tuple:
    """
    Get book data from text_file.

    It gets the book data from text_file, turns them into a tuple of book dictionaries, and replaces the empty strings
    in its key values with the text 'Missing.'

    :return: A tuple of books in dictionaries called library_tuple.
    """
    list_book_dicts = []
    text_file = 'Books_UTF.txt'
    with open(text_file, encoding='UTF-16') as text_object:
        keys = text_object.readline().strip().split()
        values = [line.strip().split('\t') for line in text_object]

        for integer in range(len(values)):
            book_dictionaries = dict(zip(keys, values[integer]))
            list_book_dicts.append(book_dictionaries)
            null_value_changer(book_dictionaries)

    library_tuple = tuple(list_book_dicts)
    return library_tuple


def null_value_changer(book_dictionaries: dict) -> dict:
    """
    Change the empty string values in each book dictionary values to 'Missing.'

    :param book_dictionaries:      A book in dictionary format with its information in key-value pairs.
    :return:                       A book in dictionary format with its null values changed to 'Missing.'

    >>> book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
    >>> null_value_changer(book) # doctest: +NORMALIZE_WHITESPACE
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}

    >>> book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': '', 'Subject': 'Comedy'}
    >>> null_value_changer(book) # doctest: +NORMALIZE_WHITESPACE
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2',
    'Category': 'Missing', 'Subject': 'Comedy'}

    >>> book = {'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''}
    >>> null_value_changer(book) # doctest: +NORMALIZE_WHITESPACE
    {'Author': 'Missing', 'Title': 'Missing', 'Publisher': 'Missing', 'Shelf': 'Missing', 'Category': 'Missing',
    'Subject': 'Missing'}
    """
    for keys in book_dictionaries:
        if book_dictionaries[f'{keys}'] == '':  # Maybe refactor this section?
            book_dictionaries[f'{keys}'] = 'Missing'
    return book_dictionaries


def menu(library_tuple: tuple) -> str:
    """
    Create menu UI for user to choose from via user input.

    ***********************************************************************

    Welcome to the Sierra Madre Library! What's your next action?

    1. I want to search.
    2. I want to move my book to somewhere else.
    3. Let me out.

    ***********************************************************************
    Enter a number between 1 and 3:

    If user chooses "I want to search," user will be led to search_handler function.
    If user chooses "I want to move my book to somewhere else," user will be led to move_handler function.
    If user chooses the last choice, user will be led to quit_program function.

    :param library_tuple:     A tuple of books in dictionary form.
    :return:                  A string value that helps exit the program.
    """
    print('*' * 100)
    print("")
    print("Welcome to the Sierra Madre Library! What's your next action?")
    print("")
    print("1. I want to search.")
    print("2. I want to move my book to somewhere else.")
    print("3. Let me out.")
    print("")
    print('*' * 100)

    eject = 'quit'

    user_decision = input("Enter a number between 1 and 3: ")
    if user_decision == '1':
        search_handler(library_tuple)
    elif user_decision == '2':
        move_handler(library_tuple)
    elif user_decision == '3':
        quit_program(library_tuple)
        return eject
    else:
        print("Please choose from 1 to 3")


def search_handler(library_tuple: tuple) -> list:  # over 20 lines! Need to shorten it down!
    """
    Search function that ask for input which will be added as a parameter for each search functions

    :param library_tuple: A tuple of books in dictionary form.
    :return:              A list of books made from search_engine function.
    """
    print("=" * 100)
    print('')
    print("These are your options: author/title/publisher/shelf/category/subject")
    print('')
    print("WARNING! Some publishers are not recorded. Therefore, you must write 'Missing' "
          "if you want to search for them.")
    print('')
    how_user_wants_to_search = input('How do you want to search? ').capitalize()
    if how_user_wants_to_search in SEARCH_CATEGORIES():
        search_input = input(f"Write down the {how_user_wants_to_search} that you want to search: ").capitalize()
        return search_engine(library_tuple, how_user_wants_to_search, search_input)
    else:
        print('Please input valid search categories.')


def decorate(search_function_that_i_want_to_decorate):  # Decorates a function
    """
    Decorate functions

    :param search_function_that_i_want_to_decorate: A function to be decorated by the wrapper.
    """

    def wrapper(list_of_books, *args, **kwargs):
        for sequence, individual_book in enumerate(list_of_books, start=1):
            print("")
            print(f"================ Result {sequence} =================")
            print(f"Author:\t\t{individual_book['Author']}")
            print(f"Title:\t\t{individual_book['Title']}")
            print(f"Publisher:\t{individual_book['Publisher']}")
            print(f"Shelf:\t\t{individual_book['Shelf']}")
            print(f"Category:\t{individual_book['Category']}")
            print(f"Subject:\t{individual_book['Subject']}")
            print("============================================")
            print("")
        return search_function_that_i_want_to_decorate(list_of_books, *args, **kwargs)

    return wrapper


def search_engine(library_tuple: tuple, search_category: str, search_input: str) -> list:
    """
    Handle search functions for all parameters without inputs.

    It handles the search function for both search and move options.

    :param library_tuple:           A tuple of books in dictionary form.
    :param search_category:         Search category in string form.
    :param search_input:            User input that decides how the search engine will search the books.
    :return:                        A list of books to be used for moving as well as searching.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transworld', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Author'
    >>> input_value = ''
    >>> search_engine(book_tuple, category, input_value)
    Please enter something.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transworld', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Author'
    >>> input_value = 'god'
    >>> search_engine(book_tuple, category, input_value)
    We regret to inform you that we have not found such books in our library.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transworld', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Author'
    >>> input_value = 'Prat'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transworld', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Author'
    >>> input_value = 'Pratchett'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2',
    'Category': 'Literature', 'Subject': 'Comedy'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transworld', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Title'
    >>> input_value = 'Guards! Guards! Guards!'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2',
    'Category': 'Literature', 'Subject': 'Comedy'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transcounty', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Publisher'
    >>> input_value = 'Transworld'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Shakespeare
    Title:      Romeo and Juliet
    Publisher:  Transworld
    Shelf:      My lap
    Category:   Literature
    Subject:    Tragedy
    ============================================
    <BLANKLINE>
    <BLANKLINE>
    ================ Result 2 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', 'Shelf': 'My lap', \
'Category': 'Literature', 'Subject': 'Tragedy'}, {'Author': 'Pratchett', \
'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2', 'Category': 'Literature', \
'Subject': 'Comedy'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transcounty', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Shelf'
    >>> input_value = '2'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2',
    'Category': 'Literature', 'Subject': 'Comedy'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transcounty', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Category'
    >>> input_value = 'Literature'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Shakespeare
    Title:      Romeo and Juliet
    Publisher:  Transworld
    Shelf:      My lap
    Category:   Literature
    Subject:    Tragedy
    ============================================
    <BLANKLINE>
    <BLANKLINE>
    ================ Result 2 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    <BLANKLINE>
    ================ Result 3 =================
    Author:     King
    Title:      It
    Publisher:  Transcounty
    Shelf:      1
    Category:   Literature
    Subject:    Horror
    ============================================
    <BLANKLINE>
    [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', 'Shelf': 'My lap', \
'Category': 'Literature', 'Subject': 'Tragedy'}, {'Author': 'Pratchett', \
'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2', 'Category': 'Literature', \
'Subject': 'Comedy'}, {'Author': 'King', 'Title': 'It', 'Publisher': 'Transcounty', 'Shelf': '1', \
'Category': 'Literature', 'Subject': 'Horror'}]

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', \
    'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}, \
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', \
    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}, \
    {'Author': 'King', 'Title': 'It', 'Publisher': 'Transcounty', \
    'Shelf': '1', 'Category': 'Literature', 'Subject': 'Horror'})
    >>> category = 'Subject'
    >>> input_value = 'Comedy'
    >>> search_engine(book_tuple, category, input_value) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    ================ Result 1 =================
    Author:     Pratchett
    Title:      Guards! Guards! Guards!
    Publisher:  Transworld
    Shelf:      2
    Category:   Literature
    Subject:    Comedy
    ============================================
    <BLANKLINE>
    [{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', 'Shelf': '2',
    'Category': 'Literature', 'Subject': 'Comedy'}]
    """
    list_of_books = []
    if search_input == '':
        print('Please enter something.')
    else:
        for book in library_tuple:
            # Extracted method
            book_input_checker(book, search_input, list_of_books, search_category)
        if list_of_books:
            # The list is needed to return so that it can be used to search parameters for move functions as well.
            # Although it returns a list, the list is not visible when the results are printed.
            return enumerate_and_help_form_decorated_results(list_of_books)
        else:
            print("We regret to inform you that we have not found such books in our library.")


# Inspired by this page in stack.overflow:
# https://stackoverflow.com/questions/13730107/writelines-writes-lines-without-newline-just-fills-the-file
def quit_program(library_tuple: tuple) -> None:
    """
    Save data and help quit program

    :param library_tuple: A tuple of books in dictionary form.
    """
    new_file = 'Books_UTF.txt'
    with open(new_file, 'w', encoding='UTF-16') as file_object:
        file_object.writelines('\t'.join(list(library_tuple[0].keys())) + '\n')
        for book in library_tuple:
            file_object.writelines('\t'.join(book.values()) + '\n')  # Is it ok to connect it with a plus sign?
    print(f"Your books have been saved in a new text file called: {new_file}.")
    print("We hope you enjoyed your stay. I hope you'll return in happier times. Until then, we'll hold you "
          "in our hearts...")


def move_handler(library_tuple: tuple) -> None:
    """
    Get necessary values before carrying out the move function.

    :param library_tuple: A tuple of books in dictionary form.
    """
    list_of_books = search_handler(library_tuple)
    if list_of_books:
        select_book_index = input("Pick which book you want to move: ")
        # Extracted method
        select_book_index_checker(list_of_books, select_book_index, library_tuple)
    else:
        print("We regret to inform you that we have not found such books in our library.")


def select_book_index_checker(list_of_books: list, select_book_index: str, library_tuple: tuple) -> None:
    """
    Check the value of select_book and see if it passes the requirements.

    After receiving list of books from move handler, it analyzes select_book_index value passed from the move handler.

    :param list_of_books:                A list of books in dictionary form.
    :param select_book_index:            Number in string form that indicates which book out of the
                                         list the user wants to move.
    :param library_tuple:                A tuple of books in dictionary form.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> book_list = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'}]
    >>> selecting_index = '0'
    >>> select_book_index_checker(book_list, selecting_index, book_tuple)  # doctest: +NORMALIZE_WHITESPACE
    My apologies, but books in that index do not exist.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> book_list = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'}]
    >>> selecting_index = 'god'
    >>> select_book_index_checker(book_list, selecting_index, book_tuple)  # doctest: +NORMALIZE_WHITESPACE
    I hate to be the bearer of bad news, but you should enter a number.
    """
    if select_book_index == '0':
        print("My apologies, but books in that index do not exist.")
    elif select_book_index.isalpha():
        print("I hate to be the bearer of bad news, but you should enter a number.")
    else:
        picking_book(library_tuple, list_of_books, select_book_index)


def book_input_checker(books: dict, book_input: str, list_of_books: list, search: str) -> None:
    """
    Check validity of the input and append books satisfying the category.

    It checks each book in the tuple to see if it matches what the user is searching for and appends them to
    an empty list called list_of_books.

    :param books:              Books in dictionary form that contains information of each book.
    :param book_input:         Search parameter of books that the user is looking for.
    :param list_of_books:      A list of books in dictionary form.
    :param search:             Search category decided by the user as to how they want to search the book.
    """
    if book_input.isdigit() and book_input == books[search]:
        list_of_books.append(books)
    elif book_input in books[search] and search != 'Shelf':
        list_of_books.append(books)
    elif book_input.isalpha() and search == 'Shelf' and (book_input == books[search] or book_input in books[search]):
        list_of_books.append(books)


@decorate
def enumerate_and_help_form_decorated_results(list_of_books: list) -> list:
    """
    Help to form a decorated result.

    A function that returns a list of books that satisfies the search result and decorates them by how it is patched.

    :param list_of_books:   A list of books that satisfies the search result.
    :return:                List of books in a series of results that are decorated by how the function is patched.
    """
    return list_of_books


def picking_book(library_tuple: tuple, list_of_books: list, select_book_index: str) -> None:
    """
    Initiate search functions to choose a book to move and then move the book.

    A function that searches a book to move after passing through initial index value requirements that it must be an
    integer and above 0.

    :param library_tuple: A tuple with dictionaries as elements
    :param list_of_books:         A list of books chosen by previous function
    :param select_book_index:     Number in string form that indicates which book out of the
                                  list the user wants to move.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> list_of_books_given = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'}]
    >>> selecting_index = '1000'
    >>> picking_book(book_tuple, list_of_books_given, selecting_index)  # doctest: +NORMALIZE_WHITESPACE
    My deepest apologies. Your input has gone beyond allotted index. Please try again.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> list_of_books_given = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'}]
    >>> selecting_index = ''
    >>> picking_book(book_tuple, list_of_books_given, selecting_index)  # doctest: +NORMALIZE_WHITESPACE
    I know it's tempting to push the boundaries, but sometimes we really must enter a number.

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> list_of_books_given = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'}]
    >>> selecting_index = 'a'
    >>> picking_book(book_tuple, list_of_books_given, selecting_index)  # doctest: +NORMALIZE_WHITESPACE
    I know it's tempting to push the boundaries, but sometimes we really must enter a number.
    """
    try:
        chosen_book = list_of_books[int(select_book_index) - 1]
    except IndexError:
        print("My deepest apologies. Your input has gone beyond allotted index. Please try again.")
    except ValueError:
        print("I know it's tempting to push the boundaries, but sometimes we really must enter a number.")
    else:
        picking_shelf(chosen_book, library_tuple)


def picking_shelf(chosen_book: dict, library_tuple: tuple) -> None:
    """Check which shelf user wants to move the book to.

    It checks which shelf the user wants to move the book, and it passes to another helper function if the
    requirements are satisfied.

    :param chosen_book:                 A dictionary that contains all the information about the chosen book.
    :param library_tuple:               A tuple of books in dictionary form.
    """
    print('')
    print(f"The book you have chosen is \n"
          f" {chosen_book['Title']} by {chosen_book['Author']}, and it is currently at Shelf "
          f"{chosen_book['Shelf']}.")
    print('')
    print("The available locations are")
    print(f"{sorted(SHELF_SET())}")
    print('')
    shelf_move = input("Which shelf do you want to move it to? ").capitalize()
    if shelf_move not in SHELF_SET():
        print('')
        print("I apologize, but you inputted an invalid shelf location. Please try again with a valid input.")
        print('')
    elif shelf_move.isalpha():
        move_book(chosen_book, shelf_move.capitalize(), library_tuple)
    else:
        move_book(chosen_book, shelf_move, library_tuple)


def move_book(chosen_book: dict, desired_shelf_location: str, library_tuple: tuple) -> None:
    """
    Move book from one location to another.

    Given that the desired shelf location is a part of the given shelf set, it moves the book to that location and
    prints helpful messages to the user that the move has been successful.

    :param chosen_book:             A book in dictionary form.
    :param desired_shelf_location:  Name of the shelf that you want to move to.
    :param library_tuple:           A tuple of books in dictionary form.
    :precondition:                  Desired shelf location must be in the constant value of SHELF_SET()

    >>> book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Shelf': 'My lap'},\
     {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}, \
     {'Author': 'King', 'Title': 'It', 'Shelf': '1'})
    >>> book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': '2'}
    >>> shelf_move = 'Noguchi'
    >>> move_book(book, shelf_move, book_tuple)  # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Congratulations, your book has been moved to Shelf Noguchi!
    <BLANKLINE>
    Take a look!
    <BLANKLINE>
    {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Shelf': 'Noguchi'}
    <BLANKLINE>
    """
    for sequence, books in enumerate(library_tuple):
        # Did this way to pass for both doctest and unit test
        if books == chosen_book or books is chosen_book:
            library_tuple[sequence]['Shelf'] = desired_shelf_location
            books['Shelf'] = desired_shelf_location
            print('')
            print(f"Congratulations, your book has been moved to Shelf {library_tuple[sequence]['Shelf']}!")
            print('')
            print("Take a look!")
            print('')
            print(f"{books}")
            print('')


def main():
    """
    Drive the program.
    """
    execute_order_66 = False
    book_collection = get_info()
    while not execute_order_66:
        menu(book_collection)
        if menu(book_collection) == 'quit':
            execute_order_66 = True


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=True)
    # Happy days