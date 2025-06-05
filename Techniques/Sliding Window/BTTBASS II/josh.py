class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=0
        total = 0
        while j < len(prices)-1:
            if prices[j] < prices[j+1]:
                total += prices[j+1] - prices[j]
            j+=1
        return total
