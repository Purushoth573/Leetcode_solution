from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        cursum = 0
        l = 0
        
        for r in range(len(nums)):
            cursum += nums[r]
            count[nums[r]] += 1
            
            # shrink if window > k
            while r - l + 1 > k:
                cursum -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l += 1   # ✅ move left pointer forward
            
            # valid window
            if r - l + 1 == k and len(count) == k:
                res = max(res, cursum)
        
        return res
