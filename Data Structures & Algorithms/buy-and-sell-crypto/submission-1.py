class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0 

        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            else:
                best = max(best, profit)
        return best 
