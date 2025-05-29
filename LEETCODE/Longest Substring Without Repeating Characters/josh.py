class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ck = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in ck:
                ck.remove(s[left])
                left+=1
            ck.add(s[right])
            print(ck)
            max_length = max(max_length, right-left+1)
        return max_length
