class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counting = 0
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                counting += 1
                i+=1
                j+=1
            else:
                j+=1
        return counting
