import unittest
from application import application

class MyTestCase(unittest.TestCase):
    def test_repeated_letter_count(self):

        self.assertEqual(application.repeated_letter_count('repppeated leter cccount'), 2)


if __name__ == '__main__':
    unittest.main()
