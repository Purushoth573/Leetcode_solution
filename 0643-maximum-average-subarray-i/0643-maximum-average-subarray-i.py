class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        cursum=0
        maxsum=0
        l=0
        for i in range(k):
            cursum+=nums[i]
        maxsum=cursum
        for i in range(k,n):
            cursum+=nums[i]
            cursum-=nums[l]
            l+=1
            maxsum=max(cursum,maxsum)
        return maxsum/k
