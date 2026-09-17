import unittest

from main import greet


class GreetingTests(unittest.TestCase):
    def test_default_name(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(greet("Python"), "Hello, Python!")


if __name__ == "__main__":
    unittest.main()
