import unittest
from application import application


class MyTestCase(unittest.TestCase):

    def test_repeated_letter_count(self):
        self.assertEqual(application.repeated_letter_count('reppeated leter cccount'), 2)

    def test_dash_insert(self):
        self.assertEqual(application.dash_insert('454793'), '4547-9-3')

    def test_mode(self):
        self.assertEqual(application.mode([1, 5, 3, 5, 2, 8, 4, 5]), 5)

    def test_super_increasing(self):
        self.assertTrue(application.super_increasing([1, 3, 6, 13, 54]))
        self.assertFalse(application.super_increasing([1, 3, 6, 13, 12]))

    def test_multi_persistence(self):
        self.assertEquals(application.multiplicative_persistence(39), 3)

    def test_match_brackets(self):
        self.assertTrue(application.matched_brackets('(())'))
        self.assertFalse(application.matched_brackets('(())((((())))'))




if __name__ == '__main__':
    unittest.main()
