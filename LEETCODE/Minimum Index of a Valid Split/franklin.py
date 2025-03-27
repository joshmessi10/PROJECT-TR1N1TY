from collections import Counter


class Solution:
    def minimumIndex(self, nums):

        for i in range(len(nums)):
            nums0 = nums[: i + 1]
            nums1 = nums[i + 1 :]

            if self.useCounter(nums0) == self.useCounter(nums1):
                return i

        return -1

    def useCounter(self, nums):
        counter = Counter(nums).most_common()

        if counter:
            dominant = counter[0][0]
            occurrences = counter[0][1]
            return dominant if occurrences * 2 > len(nums) else -1

        return -1
