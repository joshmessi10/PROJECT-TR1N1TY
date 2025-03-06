n, m = map(int, input().split())
a = list(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))

happiness = 0
for item in a:
    if item in b:
        happiness += 1
    if item in c:
        happiness -= 1

print(happiness)
