from collections import Counter
from typing import List
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = max(count, key=count.get)
        total_count = count[dominant]
        if total_count <= len(nums) // 2:
            return -1
        a_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                a_count += 1
            if a_count > (i + 1) // 2 and total_count - a_count > (len(nums) - i - 1) // 2:
                return i
        return -1   
