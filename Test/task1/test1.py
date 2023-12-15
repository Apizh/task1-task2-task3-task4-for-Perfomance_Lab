def seq(n,m):
    yield str(1)
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield str(v)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

for i in open(args.filename, 'r').read().split('\n'):
    if i:
        q = 'seq(' + i + ')'
        print(''.join(eval(q)))