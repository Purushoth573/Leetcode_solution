class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={0:1}
        cursum=0
        res=0
        for i in nums:
            cursum+=i
            if cursum-k in prefixsum:
                res+=prefixsum[cursum-k]
            if cursum in prefixsum:
                prefixsum[cursum]+=1
            else:
                prefixsum[cursum]=1
        return res

        
        