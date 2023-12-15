def min_steps(i):
    a = sorted(list(map(int, i)))
    mid = a[len(a) // 2]
    print(sum(abs(mid - j) for j in a))


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

min_steps(open(args.filename, 'r').read().split())