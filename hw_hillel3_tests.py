from hw_hillel3 import is_valid_password
from hw_hillel3 import generate_random_number


def test_valid_password():
    assert is_valid_password("Abcdefg1+")


def test_invalid_short_password():
    assert not is_valid_password("Abcd1+")


def test_generate_random_number():
    num = generate_random_number()
    assert 0 <= num <= 1000
