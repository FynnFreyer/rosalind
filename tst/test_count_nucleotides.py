import unittest
from count_nucleotides import count_occurrences


class CountNucleotidesTestCase(unittest.TestCase):
    def test_count_nucleotides_produces_sample_output(self):
        sample_input = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        sample_output = {'A': 20, 'C': 12, 'G': 17, 'T': 21}
        self.assertEqual(count_occurrences(sample_input), sample_output)


if __name__ == '__main__':
    unittest.main()
