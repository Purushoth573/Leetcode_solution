class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """maxsum = nums[0]  # handle negatives
        for i in range(len(nums)):
            sums = 0
            for j in range(i, len(nums)):
                sums += nums[j]
                maxsum = max(maxsum, sums)
        return maxsum
        """
        cursum=0
        maxsum=nums[0]

        for i in range(len(nums)):
            cursum+=nums[i]
            maxsum=max(maxsum,cursum)
            if cursum<0:
                cursum=0
        return maxsum