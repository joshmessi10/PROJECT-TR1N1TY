class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinations(index: int, path: List[int], current_sum: int):
            if current_sum == target:
                result.append(path[:])
                return
            elif current_sum > target:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                combinations(i, path, current_sum + candidates[i])  
                path.pop() 

        combinations(0, [], 0)
        return result
