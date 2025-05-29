class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        found = False

        def backtrack(index, path, indices):
            nonlocal found
            if found:
                return
            if len(path) == 2:
                if sum(path) == target:
                    result.extend(indices)
                    found = True
                return

            for i in range(index, len(numbers)):
                # Early pruning: si sum(path) + numbers[i] > target, no hace falta continuar en arreglos ordenados
                if len(path) == 1 and path[0] + numbers[i] > target:
                    break
                backtrack(i + 1, path + [numbers[i]], indices + [i + 1])

        backtrack(0, [], [])
        return result
