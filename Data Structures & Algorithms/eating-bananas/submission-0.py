class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        self.res = upperBound
        def binary(start, end) -> None:
            if start > end:
                return
            cur = 0
            mid = start + (end - start) // 2

            for pile in piles:
                cur += math.ceil(pile / mid)
            print(mid, cur)
            if cur <= h:
                self.res = min(mid, self.res)
                binary(start, mid - 1)
            else:
                binary(mid + 1, end)
        binary(1, upperBound)
        return self.res


