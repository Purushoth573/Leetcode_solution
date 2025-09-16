class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        first_neg = -1    # store index of first negative in current segment
        negcount = 0
        start = 0         # start index of current segment after a zero

        for i, n in enumerate(nums):
            if n == 0:
                first_neg = -1
                negcount = 0
                start = i + 1
            else:
                if n < 0:
                    negcount += 1
                    if first_neg == -1:
                        first_neg = i
                if negcount % 2 == 0:
                    res = max(res, i - start + 1)
                else:
                    res = max(res, i - first_neg)
        return res
        """res=0
        for l in range(len(nums)):
            product=1
            for r in range(l,len(nums)):
                product*=nums[r]
                if product>0:
                    res=max(res,r-l+1)
        return res"""
