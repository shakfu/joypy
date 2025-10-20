import unittest
from joy.utils.pretty_print import TracePrinter
from joy.utils.stack import list_to_stack

class PrettyPrintTests(unittest.TestCase):
    def test_trace_printer(self):
        tp = TracePrinter()
        tp.viewer(list_to_stack([1, 2]), list_to_stack(['+']))
        tp.viewer(list_to_stack([3]), ())
        output = str(tp)
        expected_output = "2 1 . +\n  3 . "
        self.assertEqual(output, expected_output)