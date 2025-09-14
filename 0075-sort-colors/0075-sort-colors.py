from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort colors represented by 0, 1, and 2 in-place using the Dutch National Flag algorithm.
        """
        l, r = 0, len(nums) - 1
        i = 0
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
                i += 1  # Move forward after swapping 0 to left
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                # Do NOT move i here because swapped element at i must be checked
            else:
                i += 1  # nums[i] == 1, just move on
