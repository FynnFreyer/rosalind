import unittest
from transcribe_dna2rna import transcribe_dna2rna


class TranscribeDna2RnaTestCase(unittest.TestCase):
    def test_transcribe_dna2rna_produces_sample_output(self):
        sample_input = 'GATGGAACTTGACTACGTAAATT'
        sample_output = 'GAUGGAACUUGACUACGUAAAUU'
        self.assertEqual(transcribe_dna2rna(sample_input), sample_output)

    def test_count_nucleotides_accurately_handles_empty_input(self):
        self.assertEqual(transcribe_dna2rna(''), '')


if __name__ == '__main__':
    unittest.main()
