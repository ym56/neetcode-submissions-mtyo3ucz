class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        def nonCyclicalNumber(n: int) -> bool:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            total = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                total += digit
                n = n // 10
#            for dc in str(n):
#                d = int(dc)
#                total += d ** 2
            return nonCyclicalNumber(total)


        return nonCyclicalNumber(n)