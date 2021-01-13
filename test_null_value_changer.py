from unittest import TestCase
from books import null_value_changer


class Test(TestCase):

    def test_null_value_changer_no_empty_string_inside_values(self):
        book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!',
                'Publisher': 'Transworld', 'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        expected = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Transworld',
                    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        actual = null_value_changer(book)
        self.assertEqual(expected, actual)

    def test_null_value_changer_one_empty_string_inside_values(self):
        book = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!',
                'Publisher': '', 'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        expected = {'Author': 'Pratchett', 'Title': 'Guards! Guards! Guards!', 'Publisher': 'Missing',
                    'Shelf': '2', 'Category': 'Literature', 'Subject': 'Comedy'}
        actual = null_value_changer(book)
        self.assertEqual(expected, actual)

    def test_null_value_changer_all_empty_strings_inside_values(self):
        book = {'Author': '', 'Title': '',
                'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''}
        expected = {'Author': 'Missing', 'Title': 'Missing', 'Publisher': 'Missing', 'Shelf': 'Missing',
                    'Category': 'Missing', 'Subject': 'Missing'}
        actual = null_value_changer(book)
        self.assertEqual(expected, actual)
