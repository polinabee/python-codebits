import pytest

from application import application


def test_repeated_letter_count():
    assert application.repeated_letter_count('reppeated leter cccount') == 2


@pytest.mark.parametrize("int_length", [10, 50, 100])  # tests many cases as separate tests, wow!
def testRandomIntString(int_length):
    assert type(application.randomIntString(int_length)) == str
    assert type(int(application.randomIntString(int_length))) == int


def test_dash_insert():
    assert application.dash_insert('454793') == '4547-9-3'


def testMain(mocker):
    mocker.patch('application.application.randomIntString', return_value='454793')
    assert application.final_main() == '4547-9-3'


def test_mode():
    assert application.mode([1, 5, 3, 5, 2, 8, 4, 5]) == 5


def test_super_increasing():
    assert True == application.super_increasing([1, 3, 6, 13, 54])
    assert False == application.super_increasing([1, 3, 6, 13, 12])


def test_multi_persistence():
    assert application.multiplicative_persistence(39) == 3


def test_match_brackets():
    assert True == application.matched_brackets('(())')
    assert False == application.matched_brackets('(())((((())))')
