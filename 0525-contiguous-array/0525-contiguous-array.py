class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        differencemap = {0: -1}  
        res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            diff = one - zero
            if diff in differencemap:
                res = max(res, i - differencemap[diff])
            else:
                differencemap[diff] = i

        return res
