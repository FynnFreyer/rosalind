import unittest
from fibonacci_recurrence import rabbit_recurrence


class FibonacciRecurrenceTestCase(unittest.TestCase):
    def test_rabbit_recurrence_produces_sample_output(self):
        n, k = 5, 3
        expected = 19
        self.assertEqual(rabbit_recurrence(n, k), expected)

    def test_rabbit_recurrence_accurately_handles_dataset(self):
        n, k = 36, 4
        expected = 123280631024265

        self.assertEqual(rabbit_recurrence(n, k), expected)


if __name__ == '__main__':
    unittest.main()
