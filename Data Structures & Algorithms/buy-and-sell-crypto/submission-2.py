class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        low = prices[0]
        for p in prices:
            mp = max(mp, p - low)
            low = min(p, low)
        return mp