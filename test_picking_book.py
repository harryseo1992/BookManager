from unittest import TestCase
from unittest.mock import patch
from books import picking_book
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_book_index_error(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'King Lear', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        list_of_books = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                          'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                         {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                          'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]
        select_book_index = '5'
        picking_book(book_tuple, list_of_books, select_book_index)
        expected = 'My deepest apologies. Your input has gone beyond allotted index. Please try again.\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_book_value_error(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': "Midsummer Night's Dream", 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Comedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        list_of_books = [{'Author': 'Shakespeare', 'Title': "Midsummer Night's Dream", 'Publisher': 'Transworld',
                          'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Comedy'},
                         {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                          'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]
        select_book_index = 'a'
        picking_book(book_tuple, list_of_books, select_book_index)
        expected = "I know it's tempting to push the boundaries, but sometimes we really must enter a number.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_book_value_error_empty_input(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': "Titus Andronicus", 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Comedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        list_of_books = [{'Author': 'Shakespeare', 'Title': 'Titus Andronicus', 'Publisher': 'Transworld',
                          'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Comedy'},
                         {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                          'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]
        select_book_index = ''
        picking_book(book_tuple, list_of_books, select_book_index)
        expected = "I know it's tempting to push the boundaries, but sometimes we really must enter a number.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
