class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join([s[x] if s[x].isalnum() else " " for x in range(len(s))]).lower().replace(" ", "")
        word2 = "".join([s[x] if s[x].isalnum() else " " for x in range(len(s)-1,-1,-1)]).lower().replace(" ", "")
        return True if word == word2 else False
