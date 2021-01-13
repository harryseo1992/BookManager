from unittest import TestCase
from unittest.mock import patch
from books import search_handler
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['pearly gates'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_handler_wrong_input(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Othello', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_handler(book_tuple)
        expected = "======================================================================" \
                   "==============================\n\n" \
                   "These are your options: author/title/publisher/shelf/category/subject\n\n" \
                   "WARNING! Some publishers are not recorded. Therefore, you must write 'Missing' " \
                   "if you want to search for them.\n\n" \
                   "Please input valid search categories.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_handler_empty_input(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_handler(book_tuple)
        expected = "======================================================================" \
                   "==============================\n\n" \
                   "These are your options: author/title/publisher/shelf/category/subject\n\n" \
                   "WARNING! Some publishers are not recorded. Therefore, you must write 'Missing' " \
                   "if you want to search for them.\n\n" \
                   "Please input valid search categories.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
