class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        window=len(nums)+1
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                window=min(window,r-l+1)
                cursum-=nums[l]
                l+=1
        return 0 if window == len(nums) + 1 else window
