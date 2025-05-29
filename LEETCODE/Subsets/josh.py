class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def calculating(index, path):
            results.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                calculating(i+1, path)
                path.pop()
        calculating(0,[])
        return results
