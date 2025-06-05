class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            save = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
            s[i] = save
