from unittest import TestCase
from unittest.mock import patch
from books import search_engine
import io


class TestSearchEngine(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_empty_search_input(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Othello', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Author'
        search_input = ''
        search_engine(book_tuple, search_category, search_input)
        expected = "Please enter something.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_but_book_does_not_exist(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Titus Andronicus', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Author'
        search_input = 'Tolstoy'
        search_engine(book_tuple, search_category, search_input)
        expected = "We regret to inform you that we have not found such books in our library.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_author_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Author'
        search_input = 'Shakespeare'
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_title_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Title'
        search_input = 'Romeo and Juliet'
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_publisher_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Publisher'
        search_input = 'Transworld'
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n" \
                   "\n================ Result 2 =================\n" \
                   "Author:		Pratchett\n" \
                   "Title:		Guards! Guards! Guards!\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		2\n" \
                   "Category:	Literature\n" \
                   "Subject:	Comedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_shelf_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Shelf'
        search_input = 'Moon'
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_category_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Category'
        search_input = "Literature"
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n" \
                   "\n================ Result 2 =================\n" \
                   "Author:		Pratchett\n" \
                   "Title:		Guards! Guards! Guards!\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		2\n" \
                   "Category:	Literature\n" \
                   "Subject:	Comedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_engine_right_search_input_subject_search(self, mock_stdout):
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'Moon', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        search_category = 'Subject'
        search_input = "Tragedy"
        search_engine(book_tuple, search_category, search_input)
        expected = "\n================ Result 1 =================\n" \
                   "Author:		Shakespeare\n" \
                   "Title:		Romeo and Juliet\n" \
                   "Publisher:	Transworld\n" \
                   "Shelf:		Moon\n" \
                   "Category:	Literature\n" \
                   "Subject:	Tragedy\n" \
                   "============================================\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
