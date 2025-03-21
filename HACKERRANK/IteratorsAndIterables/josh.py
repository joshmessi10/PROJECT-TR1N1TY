import itertools

def problem():
    n = int(input())
    a = input().strip().replace(" ", "") 
    k = int(input())
    combinations = list(itertools.combinations(a, k))
    letter = 'a'
    count = 0
    for combo in combinations:
        if letter in combo:
            count += 1
    result = count / len(combinations)
    print(f"{result:.3f}")

if __name__ == '__main__':
    problem()
