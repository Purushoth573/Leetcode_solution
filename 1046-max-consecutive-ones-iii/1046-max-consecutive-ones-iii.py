class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        no_of_zero=0
        maxnum=0
        for r in range(len(nums)):
            if nums[r]==0:
                no_of_zero+=1
            while no_of_zero>k:
                if nums[l]==0:
                    no_of_zero-=1
                l+=1
            maxnum=max(maxnum,r-l+1)
                
        return maxnum
        