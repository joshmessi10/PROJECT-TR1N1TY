# First Try
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counting = 0
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        while n > 0 and m > 0:
            if g[0] <= s[0]:
                counting += 1
                g.pop(0)
                s.pop(0)
                n-=1
                m-=1
            else:
                s.pop(0)
                m-=1
        return counting

