class Solution:
    def mostPoints(self, questions):
        hash_map = {}
        return self.mostPoints_(hash_map, 0, questions)

    def mostPoints_(self, hash_map, index, questions):
        if not questions:
            return 0

        if hash_map.get(index, 0):
            return hash_map[index]

        points, jump = questions[0]

        taken = points + self.mostPoints_(
            hash_map, index + jump + 1, questions[jump + 1 :]
        )
        not_taken = self.mostPoints_(hash_map, index + 1, questions[1:])

        hash_map[index] = max(taken, not_taken)
        return hash_map[index]


solution = Solution()
print(solution.mostPoints([[72,5],[36,5],[95,5],[50,1],[62,1],[14,3],[72,5],[86,2],[43,3],[51,3],[14,1],[91,5],[47,4],[72,4],[63,5],[40,3],[68,1],[8,3],[84,5],[7,5],[40,1],[35,3],[66,2],[39,5],[40,1],[92,3],[67,5],[34,3],[84,4],[75,5],[6,1],[71,3],[77,3],[25,3],[53,3],[32,3],[88,5],[18,2],[21,3],[78,2],[69,5],[45,4],[94,2],[70,1],[85,2],[7,2],[68,4],[71,4],[57,2],[12,5],[53,5],[51,3],[46,1],[28,3]]))
