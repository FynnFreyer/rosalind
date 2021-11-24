#!/usr/bin/env python3

import argparse
from typing import Dict
from collections import defaultdict


# this is total overkill, sys.argv[1] would probably have sufficed, but helpful messages are nice
def parse_args():
    parser = argparse.ArgumentParser(description='Count the character occurrences in a (nucleotide) string')

    parser.add_argument('nucleotide_string', help='(nucleotide) string of which to count the character occurrences')

    return parser.parse_args()


def count_occurrences(string: str) -> Dict[str, int]:
    results_dict = defaultdict(lambda: 0)
    for character in string:
        results_dict[character] += 1
    return dict(results_dict)


if __name__ == "__main__":
    args = parse_args()
    print(count_occurrences(args.nucleotide_string))
