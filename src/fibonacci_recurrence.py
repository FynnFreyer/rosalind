#!/usr/bin/env python3

import argparse


# here is something where argparse shines
def parse_args():
    parser = argparse.ArgumentParser(description='Calculate the number of rabbits with k-sized litters after n months')

    parser.add_argument('n', type=int, help='months that pass')
    parser.add_argument('k', type=int, help='reproductive age rabbits have this big a litter every month')

    return parser.parse_args()


def rabbit_recurrence(months: int, litter_size: int) -> int:
    reproductive_rabbits = 0  # F_0
    newborn_rabbits = 1  # F_1

    for _ in range(months):
        new_litter = reproductive_rabbits * litter_size
        maturing_rabbits = newborn_rabbits
        reproductive_rabbits += maturing_rabbits
        newborn_rabbits = new_litter

    return reproductive_rabbits


if __name__ == "__main__":
    args = parse_args()
    print(rabbit_recurrence(args.n, args.k))
