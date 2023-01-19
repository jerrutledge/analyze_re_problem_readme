import unittest
import compute
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

test_list = [
    {"threshold": 0, "limit": 0, "input": [], "output": "0.0\n"},
    {"threshold": 0, "limit": 0, "input": ["0"], "output": "0.0\n0.0\n"},
    {"threshold": 0, "limit": 0, "input": ["5"], "output": "0.0\n0.0\n"},
    {"threshold": 0, "limit": 10, "input": ["5"], "output": "5.0\n5.0\n"},
    {"threshold": 1000000000, "limit": 1000000000, "input": [], "output": "0.0\n"},
    {"threshold": 1000000000, "limit": 1000000000,
        "input": ["0"], "output": "0.0\n0.0\n"},
    {"threshold": 0, "limit": 1000000000, "input": [
        1000000000], "output": "1000000000.0\n1000000000.0\n"},
    {"threshold": 0, "limit": 1000000000, "input": [
        1000000000, 100], "output": "1000000000.0\n0.0\n1000000000.0\n"},
    {"threshold": 0, "limit": 100, "input": [
        0.0, 10.0, 50.0, 50.0, 10.0, 20.0], "output": "0.0\n10.0\n50.0\n40.0\n0.0\n0.0\n100.0\n"}
]


class TestProcessMethod(TestCase):
    def test_inputs(self):
        for test in test_list:
            with self.subTest():
                with patch('sys.stdout', new=StringIO()) as output:
                    compute.Compute.process(
                        test["threshold"], test["limit"], test["input"])
                    self.assertEqual(output.getvalue(), test["output"])


if __name__ == "__main__":
    unittest.main()
