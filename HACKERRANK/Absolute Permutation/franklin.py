from sys import exit


def getResult(i, pos, available):
    result = list()
    len_avail = len(available)

    while i < len(pos):
        per_1 = abs(-k - pos[i])  # -1 - 1 = - 2
        per_2 = abs(k - pos[i])  # 1 - 1 = 0
        candidates = [False, False]

        if (
            per_1 > 0
            and per_1 <= len_avail
            and available[per_1 - 1] != -1
            and abs(pos[i] - per_1) == k
        ):
            candidates[0] = True

        if (
            per_1 != per_2
            and per_2 > 0
            and per_2 <= len_avail
            and available[per_2 - 1] != -1
            and abs(pos[i] - per_2) == k
        ):
            candidates[1] = True

        if not any(candidates):
            return [-1]

        if candidates[0] and not candidates[1]:
            result.append(per_1)
            available[per_1 - 1] = -1

        if not candidates[0] and candidates[1]:
            result.append(per_2)
            available[per_2 - 1] = -1

        if all(candidates):
            available_1_copy = available.copy()
            available_2_copy = available.copy()

            available_1_copy[per_1 - 1] = -1
            available_2_copy[per_2 - 1] = -1

            result_1 = result + [per_1] + getResult(i + 1, pos, available_1_copy)
            result_2 = result + [per_2] + getResult(i + 1, pos, available_2_copy)

            return min(result_1, result_2)

        i += 1

    return result


def absolutePermutation(n, k):
    pos = list(range(1, n + 1))
    return getResult(0, pos, pos.copy())


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        my_input = list(map(int, input().split()))

        n = int(my_input[0])

        k = int(my_input[1])

        result = absolutePermutation(n, k)

        print(result)

"""
TODO:

CHECK IF ELEMENT IS AVAILABLE TO BE TAKEN FROM POS = [1,2,3,-1,5,6] (4 NOT AVAILABLE)
"""
