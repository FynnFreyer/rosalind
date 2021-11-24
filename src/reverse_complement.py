#!/usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compute the reverse complement of a DNA string')

    parser.add_argument('dna_string', help='(DNA) string to compute the reverse complement of')

    return parser.parse_args()


def reverse_complement(dna_string: str) -> str:
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement_string = ''
    for base in dna_string[::-1]:
        reverse_complement_string += complements[base]
    return reverse_complement_string


if __name__ == "__main__":
    args = parse_args()
    print(reverse_complement(args.dna_string))
