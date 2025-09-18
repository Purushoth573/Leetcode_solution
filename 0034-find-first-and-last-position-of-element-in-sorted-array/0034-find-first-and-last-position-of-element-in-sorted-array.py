from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            first = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1  # keep searching left
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first
        
        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            last = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1  # keep searching right
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return last
        
        return [findFirst(nums, target), findLast(nums, target)]"""
        def binarySearch(leftBias: bool) -> int:
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    idx = mid
                    if leftBias:
                        r = mid - 1  # search left side
                    else:
                        l = mid + 1  # search right side
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
        
        return [binarySearch(True), binarySearch(False)]

