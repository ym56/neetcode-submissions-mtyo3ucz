class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenNums = len(numbers)
        s, e = 0, lenNums - 1

        while s < e:
            num1, num2 = numbers[s], numbers[e]
            if num1 + num2 == target:
                return [s + 1, e + 1]
            if num1 + num2 > target:
                e -= 1
            else:
                s += 1
        return []