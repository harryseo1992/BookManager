from unittest import TestCase
from unittest.mock import patch
from books import select_book_index_checker
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_book_index_checker_zero_index(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Othello', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        list_of_books = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                          'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                         {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                          'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]
        select_book_index = '0'
        select_book_index_checker(list_of_books, select_book_index, book_tuple)
        expected = 'My apologies, but books in that index do not exist.\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_book_index_checker_alphabet_index(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        list_of_books = [{'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                          'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                         {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                          'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}]
        select_book_index = 'god'
        select_book_index_checker(list_of_books, select_book_index, book_tuple)
        expected = 'I hate to be the bearer of bad news, but you should enter a number.\n'
        self.assertEqual(expected, mock_stdout.getvalue())
