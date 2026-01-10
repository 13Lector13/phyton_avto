import unittest
from lesson_12.homework_12 import (
    numbers_sum,
    avg_func,
    reverse_string,
    longest_word,
    find_substring
)



class TestNumbersSum(unittest.TestCase):
    def test_numbers_sum(self):
        expected = 11
        result = numbers_sum(5,6)
        self.assertEqual(result, expected)

        self.assertIsNotNone(result)

class TestNumbersSumNegative(unittest.TestCase):
    def test_numbers_sum(self):
        expected = 11
        result = numbers_sum(-5, -6)
        self.assertNotEqual(result, expected)

        self.assertIsNotNone(result)



class TestAvgFunc(unittest.TestCase):
    def test_avg_func(self):
        expected = 6
        result = avg_func([5, 6, 7])
        self.assertEqual(result, expected)

        self.assertIsNotNone(result)

class TestAvgFuncNegative(unittest.TestCase):
    def test_avg_func_invalid_data(self):
        with self.assertRaises(TypeError):
            avg_func(['a', 0, 'a7'])




class TestReverseString(unittest.TestCase):
    def test_string(self):
        expected = "olleH"
        result = reverse_string("Hello")
        self.assertEqual(result, expected)

        self.assertIsNotNone(result)

class TestReverseStringNegative(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(ValueError):
            reverse_string("")


class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        expected= "Goodbye"
        result = longest_word("Hello, world! Goodbye, world!")
        self.assertEqual(result, expected)

        self.assertIsNotNone(result)

class TestLongestWordNegative(unittest.TestCase):
    def test_longest_word_empty(self):
        with self.assertRaises(ValueError):
            longest_word(" ")



class TestFindSubstringFound(unittest.TestCase):
    def test_find_substring(self):
        expected = 7
        result = find_substring("Hello, world!", "world")
        self.assertEqual(result, expected)

class TestFindSubstringNotFound(unittest.TestCase):
    def test_find_substring(self):
        expected = -1
        result = find_substring(
            "The quick brown fox jumps over the lazy dog",
            "cat"
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
