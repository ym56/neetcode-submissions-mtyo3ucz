class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        bought = prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] - bought)
            bought = min(bought, prices[i])
        
        return res