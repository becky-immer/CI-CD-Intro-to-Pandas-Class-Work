import unittest
from src import main

class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert main.add(2,3) == 5
        print("Add function works properly")


if __name__ == "__main__":
    unittest.main