def min_steps(i):
    a = sorted(list(map(int, i)))
    mid = a[len(a) // 2]
    print(sum(abs(mid - j) for j in a))


min_steps(open(input().strip('"').strip("'") , 'r').read().split('\n'))