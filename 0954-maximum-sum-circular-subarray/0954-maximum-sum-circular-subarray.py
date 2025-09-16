class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax,gmin=nums[0],nums[0]
        cmax,cmin=0,0
        total=0
        for n in nums:
            cmax=max(cmax+n,n)
            cmin=min(cmin+n,n)
            total+=n
            gmax=max(cmax,gmax)
            gmin=min (cmin,gmin)
        if gmax < 0:
            return gmax
        return max(gmax,total-gmin)

        