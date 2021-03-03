import unittest
from application import application

class MyTestCase(unittest.TestCase):
    def test_repeated_letter_count(self):

        self.assertEqual(application.repeated_letter_count('reppeated leter cccount'), 2)

    def test_dash_insert(self):

        self.assertEqual(application.dash_insert('454793'),'4547-9-3')


if __name__ == '__main__':
    unittest.main()
