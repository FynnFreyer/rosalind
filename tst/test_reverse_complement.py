import unittest
from reverse_complement import reverse_complement


class ReverseComplementTestCase(unittest.TestCase):
    def test_count_nucleotides_produces_sample_output(self):
        sample_input = 'AAAACCCGGT'
        sample_output = 'ACCGGGTTTT'
        self.assertEqual(reverse_complement(sample_input), sample_output)

    def test_count_nucleotides_accurately_handles_empty_input(self):
        self.assertEqual(reverse_complement(''), '')


if __name__ == '__main__':
    unittest.main()
