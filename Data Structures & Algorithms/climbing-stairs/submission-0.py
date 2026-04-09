class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * n

        def step(i: int):
            if i >= n:
                return i == n
            if dp[i] != -1:
                return dp[i]
            dp[i] = step(i + 1) + step(i +2)
            return dp[i]


        return step(0)