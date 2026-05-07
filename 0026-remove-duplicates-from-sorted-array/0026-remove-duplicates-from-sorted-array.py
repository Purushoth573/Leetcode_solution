from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

        return l + 1


# Input
nums = [1, 1, 2, 2, 3, 4, 4, 5]

print("Running Remove Duplicates Program")
print("Input Array:", nums)

obj = Solution()

k = obj.removeDuplicates(nums)

print("Number of Unique Elements:", k)
print("Array After Removing Duplicates:", nums[:k])
