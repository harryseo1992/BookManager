from unittest import TestCase
from unittest.mock import patch
from books import move_handler
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['god'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_handler_wrong_input(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        move_handler(book_tuple)
        expected = "======================================================================" \
                   "==============================\n\n" \
                   "These are your options: author/title/publisher/shelf/category/subject\n\n" \
                   "WARNING! Some publishers are not recorded. Therefore, you must write 'Missing' " \
                   "if you want to search for them.\n\n" \
                   "Please input valid search categories.\n" \
                   "We regret to inform you that we have not found such books in our library.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_handler_empty_input(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'MacBeth', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        move_handler(book_tuple)
        expected = "======================================================================" \
                   "==============================\n\n" \
                   "These are your options: author/title/publisher/shelf/category/subject\n\n" \
                   "WARNING! Some publishers are not recorded. Therefore, you must write 'Missing' " \
                   "if you want to search for them.\n\n" \
                   "Please input valid search categories.\n" \
                   "We regret to inform you that we have not found such books in our library.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
