class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        gmax = cmax = cmin = nums[0]
        for n in nums[1:]:
            tmp = cmax
            cmax = max(n, cmax * n, cmin * n)
            cmin = min(n, tmp * n, cmin * n)
            gmax = max(gmax, cmax)
        return gmax
