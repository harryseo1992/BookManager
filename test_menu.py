from unittest import TestCase
from unittest.mock import patch
from books import menu
import io


class TestMenu(TestCase):
    
    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_invalid_input(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Othello', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        menu(book_tuple)
        expected = "************************************************************************************" \
                   "****************\n\nWelcome to the Sierra Madre Library! What's your next action?\n\n" \
                   "1. I want to search.\n" \
                   "2. I want to move my book to somewhere else.\n" \
                   "3. Let me out.\n\n" \
                   "**********************************************************************************" \
                   "******************\n" \
                   "Please choose from 1 to 3\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_empty_string(self, mock_stdout, mock_input):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        menu(book_tuple)
        expected = "************************************************************************************" \
                   "****************\n\nWelcome to the Sierra Madre Library! What's your next action?\n\n" \
                   "1. I want to search.\n" \
                   "2. I want to move my book to somewhere else.\n" \
                   "3. Let me out.\n\n" \
                   "**********************************************************************************" \
                   "******************\n" \
                   "Please choose from 1 to 3\n"
        self.assertEqual(expected, mock_stdout.getvalue())
