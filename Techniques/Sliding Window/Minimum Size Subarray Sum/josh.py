class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cum = 0
        left = 0
        min_length = float('inf')
        for right in range(0,len(nums)):
            cum += nums[right]
            while cum >= target:
                if cum >= target:
                    min_length = min(min_length, right-left+1)
                cum -= nums[left]
                left +=1
            #print(arr)
        if min_length == float('inf'):
            min_length = 0
        return min_length
        
