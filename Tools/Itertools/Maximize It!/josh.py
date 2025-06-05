import itertools
k, m = map(int, input().strip().split())
X = []
for i in range(k):
    X.append(list(map(int, input().strip().split())))

X = [i[1:] for i in X]
combinaciones = itertools.product(*X)
resultados = list(map(lambda arr: sum(x**2 for x in arr)%(m), combinaciones))
print(max(resultados))
