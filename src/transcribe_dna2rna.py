#!/usr/bin/env python3

import argparse


# sys.argv[1] would have sufficed again, but helpful messages are still nice
def parse_args():
    parser = argparse.ArgumentParser(description='Transcribe DNA strings into RNA strings')

    parser.add_argument('dna_string', help='(DNA) string to transcribe to RNA')

    return parser.parse_args()


def transcribe_dna2rna(dna_string: str) -> str:
    rna_string = dna_string.replace('T', 'U')
    # or e.g. with a list comprehension
    # rna_string = [base if base != 'T' else 'U' for base in dna_string]
    return rna_string


if __name__ == "__main__":
    args = parse_args()
    print(transcribe_dna2rna(args.dna_string))
