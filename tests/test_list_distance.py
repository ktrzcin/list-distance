import pathlib
import unittest
from contextlib import contextmanager
from unittest.mock import patch

from list_distance import calculate_distance

PATH: str = pathlib.Path(__file__).parent.absolute() / "fixtures/"


@contextmanager
def patched_stdin(filename: str) -> None:
    """
    Patch stdin to yield values from file.
    """
    with open(PATH / filename) as fd:
        with patch("sys.stdin", fd):
            yield


class TestValidInput(unittest.TestCase):
    def test_valid_input1(self):
        with patched_stdin("valid_input1.txt"):
            self.assertEqual(calculate_distance(), 0)

    def test_valid_input2(self):
        with patched_stdin("valid_input2.txt"):
            self.assertEqual(calculate_distance(), 5)

    def test_valid_input3(self):
        with patched_stdin("valid_input3.txt"):
            self.assertEqual(calculate_distance(), 1)


class TestArgsCountMismatch(unittest.TestCase):
    def assertValueError(self):
        with self.assertRaises(ValueError):
            calculate_distance()

    def test_too_few_args(self):
        with patched_stdin("too_few_args.txt"):
            self.assertValueError()

    def test_too_few_list_a_elements(self):
        with patched_stdin("too_few_list_a_elements.txt"):
            self.assertValueError()

    def test_too_few_list_b_elements(self):
        with patched_stdin("too_few_list_b_elements.txt"):
            self.assertValueError()

    def test_too_many_args(self):
        with patched_stdin("too_many_args.txt"):
            self.assertValueError()

    def test_too_many_list_a_elements(self):
        with patched_stdin("too_many_list_a_elements.txt"):
            self.assertValueError()

    def test_too_many_list_b_elements(self):
        with patched_stdin("too_many_list_b_elements.txt"):
            self.assertValueError()


class MiscellaneousErrors(unittest.TestCase):
    def test_unexpected_eof(self):
        with patched_stdin("unexpected_eof.txt"):
            with self.assertRaises(EOFError):
                calculate_distance()

    def test_char_in_args(self):
        with patched_stdin("char_in_args.txt"):
            with self.assertRaises(ValueError):
                calculate_distance()

    def test_float_in_args(self):
        with patched_stdin("float_in_args.txt"):
            with self.assertRaises(ValueError):
                calculate_distance()
