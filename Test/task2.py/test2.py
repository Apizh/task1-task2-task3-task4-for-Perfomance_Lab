


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

adres = open(args.filename, 'r').read().strip().split()
rad = open(adres[0], 'r').read().strip().split('\n')
points = open(adres[1], 'r').read().strip().split('\n')
top_point = float(rad[-1]) + sum(map(lambda x: float(x) ** 2, rad[0].split())) ** 0.5
bot_point = float(rad[-1]) - sum(map(lambda x: float(x) ** 2, rad[0].split())) ** 0.5

for point in points:
    hyp = sum(map(lambda x: float(x) ** 2, point.split())) ** 0.5

    if not(hyp): print('точка лежит на окружности')

    else: print('точка', ('снаружи', 'внутри')[bot_point <= hyp <= top_point])