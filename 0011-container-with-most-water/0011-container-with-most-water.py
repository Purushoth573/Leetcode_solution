from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxarea = max(maxarea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea


# Input
height = [1,8,6,2,5,4,8,3,7]

print("Running Container With Most Water Program")
print("Input Array:", height)

obj = Solution()
result = obj.maxArea(height)

print("Maximum Water Container Area:", result)
