from unittest import TestCase
from books import move_book
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_shakespeare(self, mock_stdout):
        chosen_book = {'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'}
        desired_shelf_location = 'Noguchi'
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        move_book(chosen_book, desired_shelf_location, book_tuple)
        expected = "\nCongratulations, your book has been moved to Shelf Noguchi!\n\n" \
                   "Take a look!\n\n" \
                   "{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld', " \
                   "'Shelf': 'Noguchi', 'Category': 'Literature', 'Subject': 'Tragedy'}\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_pratchett(self, mock_stdout):
        chosen_book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        desired_shelf_location = 'Reading'
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Mark Antony', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        move_book(chosen_book, desired_shelf_location, book_tuple)
        expected = "\nCongratulations, your book has been moved to Shelf Reading!\n\n" \
                   "Take a look!\n\n" \
                   "{'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld', " \
                   "'Shelf': 'Reading', 'Category': 'Literature', 'Subject': 'Comedy'}\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
