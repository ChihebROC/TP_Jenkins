#!/usr/bin/env python3

from reverse import reverse_name
import unittest

class TestReverse(unittest.TestCase):
  
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(reverse_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(reverse_name(testcase), expected)

  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(reverse_name(testcase), expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(reverse_name(testcase), expected)

# Run the tests
unittest.main()
