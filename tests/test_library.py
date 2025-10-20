import unittest
from joy.library import initialize
from joy.joy import run
from joy.utils.stack import list_to_stack

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = initialize()

    def test_initialize(self):
        self.assertIn('+', self.dictionary)
        self.assertIn('dup', self.dictionary)
        self.assertIn('swap', self.dictionary)
        self.assertIn('pop', self.dictionary)

    def test_dup(self):
        stack, _, _ = run("dup", list_to_stack([1]), self.dictionary)
        self.assertEqual(stack, list_to_stack([1, 1]))

    def test_swap(self):
        stack, _, _ = run("swap", list_to_stack([1, 2]), self.dictionary)
        self.assertEqual(stack, list_to_stack([2, 1]))

    def test_pop(self):
        stack, _, _ = run("pop", list_to_stack([1, 2]), self.dictionary)
        self.assertEqual(stack, list_to_stack([2]))

    def test_add(self):
        stack, _, _ = run("+", list_to_stack([1, 2]), self.dictionary)
        self.assertEqual(stack, list_to_stack([3]))