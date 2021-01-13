from unittest import TestCase
from unittest.mock import patch
from books import picking_shelf
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_shelf_empty_shelf_move_input(self, mock_stdout, mock_input):
        chosen_book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Romeo and Juliet', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        picking_shelf(chosen_book, book_tuple)
        expected = "\nThe book you have chosen is \n" \
                   " Guards! Guards! Guards! by Pratchett, and it is currently at Shelf 2.\n\n" \
                   "The available locations are\n" \
                   "['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', " \
                   "'24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', " \
                   "'4', '5', '6', '7', '8', '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n\n" \
                   "I apologize, but you inputted an invalid shelf location. Please try again with a valid input.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['pearly gates'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_shelf_wrong_shelf_move_input(self, mock_stdout, mock_input):
        chosen_book = {'Author': 'Pratchett', 'Title': 'The Thief of Time', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'Othello', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        picking_shelf(chosen_book, book_tuple)
        expected = "\nThe book you have chosen is \n" \
                   " The Thief of Time by Pratchett, and it is currently at Shelf 2.\n\n" \
                   "The available locations are\n" \
                   "['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', " \
                   "'24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', " \
                   "'4', '5', '6', '7', '8', '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n\n" \
                   "I apologize, but you inputted an invalid shelf location. Please try again with a valid input.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['Noguchi'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_picking_shelf_right_shelf_move_input(self, mock_stdout, mock_input):
        chosen_book = {'Author': 'Pratchett', 'Title': 'Mort', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        book_tuple = ({'Author': 'Shakespeare', 'Title': 'King Lear', 'Publisher': 'Transworld',
                       'Shelf': 'My lap', 'Category': 'Literature', 'Subject': 'Tragedy'},
                      {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                       'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'})
        picking_shelf(chosen_book, book_tuple)
        expected = "\nThe book you have chosen is \n" \
                   " The Thief of Time by Pratchett, and it is currently at Shelf 2.\n\n" \
                   "The available locations are\n" \
                   "['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', " \
                   "'24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', " \
                   "'4', '5', '6', '7', '8', '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
