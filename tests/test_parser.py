import unittest
from joy.parser import text_to_expression, Symbol
from joy.utils.stack import list_to_stack

class ParserTests(unittest.TestCase):
    def test_simple_expression(self):
        # Test a simple expression with integers and a symbol
        expression = text_to_expression("1 2 +")
        self.assertEqual(expression, list_to_stack([1, 2, Symbol('+')]))

    def test_nested_expression(self):
        # Test a nested expression with lists
        expression = text_to_expression("[1 2] [3 4] concat")
        expected = list_to_stack([
            list_to_stack([1, 2]),
            list_to_stack([3, 4]),
            Symbol('concat')
        ])
        self.assertEqual(expression, expected)

    def test_string_literal(self):
        # Test a string literal
        expression = text_to_expression('"hello world"')
        self.assertEqual(expression, list_to_stack(['hello world']))

    def test_empty_input(self):
        # Test an empty input string
        expression = text_to_expression("")
        self.assertEqual(expression, ())

    def test_unbalanced_brackets(self):
        # Test unbalanced brackets
        with self.assertRaises(Exception):
            text_to_expression("[1 2")

    def test_extra_closing_bracket(self):
        # Test extra closing bracket
        with self.assertRaises(Exception):
            text_to_expression("1 2]")