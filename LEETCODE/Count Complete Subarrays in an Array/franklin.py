class Solution:
    def countCompleteSubarrays(self, nums):
        subarrays = 0
        len_nums = len(nums)
        unique_nums = set(nums)
        min_window = len(unique_nums)

        while min_window < len_nums:
            range_ = len_nums - min_window
            j = 0
            
            for i in range(range_):
                while j <= len_nums - min_window:
                    if unique_nums == set(nums[j:j+min_window]):
                        subarrays += 1
                        
                    j += 1

            min_window += 1

        return subarrays + 1

solution = Solution()
result = solution.countCompleteSubarrays([5,5,5,5])
print(result)
