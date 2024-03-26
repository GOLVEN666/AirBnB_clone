#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for the HBNBCommand class."""

    def test_prompt(self):
        """Test if the prompt is set correctly."""
        console = HBNBCommand()
        self.assertEqual("(hbnb) ", console.prompt)


if __name__ == "__main__":
    unittest.main()

