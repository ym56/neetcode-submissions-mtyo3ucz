class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        rem = False
        for i in range(len(digits) - 1, -1, -1):
            cindyIsCute = digits[i]
            if rem and cindyIsCute + 1 > 9:
                rem = True
                res.insert(0, 0)
            elif i == len(digits) - 1:
                if (cindyIsCute + 1 > 9):
                    rem = True
                    res.insert(0, 0)
                else:
                    res.insert(0, cindyIsCute + 1)
            else:
                if rem:
                    res.insert(0, cindyIsCute + 1)
                else:
                    res.insert(0, cindyIsCute)
                rem = False
        if (rem):
            res.insert(0, 1)
        return res
