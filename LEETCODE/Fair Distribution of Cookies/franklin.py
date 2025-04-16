from itertools import combinations, permutations

class Solution:
    def distributeCookies(self, cookies, k):
        range_ = range(len(cookies))
        comb = list(combinations(range_, k))
        per = list(permutations(cookies, len(cookies)))

        m = 2

        for e in comb[0][1:]:
            m += range_[-1] - e

        minimum = -1
        maximum = -1
        
        for p in range(len(per)):
            for c in range(len(comb[:m])):
                differences = []
                
                for i in range(len(comb[c])):
                    if i == k - 1:
                        differences.append(sum(per[p][comb[c][i]:]))
                        break

                    differences.append(sum(per[p][comb[c][i]: comb[c][i + 1]]))
                
                max_diff = max(differences)
                mini_diff = max_diff - min(differences)

                if minimum == -1:
                    minimum = mini_diff
                    maximum = max_diff
                
                elif mini_diff < minimum:
                    minimum = mini_diff
                    maximum = max_diff

        return maximum

solution = Solution()
result = solution.distributeCookies([941, 797, 1475, 638, 191, 712], 3)
print(result)