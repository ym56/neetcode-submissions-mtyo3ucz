class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def chomp(eatingRate):
            res = 0
            for p in piles:
                res += math.ceil(float(p) / eatingRate)
            return res <= h


        res = float('inf')
        largestPile = max(piles)
        l, r = 1, largestPile

        while l <= r:
            mid = l + (r - l) // 2
            isValid = chomp(mid)
            if isValid:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        print(res)
        return res
