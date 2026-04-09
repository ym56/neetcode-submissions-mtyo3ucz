class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        while True:
            print(b)
            if a >= b:
                return True
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            if s[a].lower() != s[b].lower():
                print(s[a])
                print(s[b])
                return False
            a += 1
            b -= 1
            
