
import unittest
from joy.joy import joy, run
from joy.library import initialize
from joy.utils.stack import list_to_stack
from joy.parser import text_to_expression

class JoyTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = initialize()

    def test_joy_function(self):
        # Test the joy function directly
        stack, _, _ = joy(list_to_stack([1, 2]), text_to_expression('+'), self.dictionary)
        self.assertEqual(stack, list_to_stack([3]))

    def test_run_function(self):
        # Test the run function with a simple program
        stack, _, _ = run('1 2 +', (), self.dictionary)
        self.assertEqual(stack, list_to_stack([3]))

    def test_run_with_initial_stack(self):
        # Test the run function with an initial stack
        stack, _, _ = run('+', list_to_stack([1, 2]), self.dictionary)
        self.assertEqual(stack, list_to_stack([3]))

    def test_run_with_unbalanced_brackets(self):
        # Test run function with unbalanced brackets
        stack, _, _ = run('[', (), self.dictionary)
        self.assertEqual(stack, ())
