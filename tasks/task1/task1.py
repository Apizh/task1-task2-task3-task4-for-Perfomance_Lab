def seq(n,m):
    yield str(1)
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield str(v)

n, m = map(int, input().split())
out = seq(n, m)


print(''.join(out))