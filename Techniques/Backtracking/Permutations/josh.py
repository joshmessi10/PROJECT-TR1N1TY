class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permutations(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                permutations(path)
                path.pop()
        permutations([])
        return result
