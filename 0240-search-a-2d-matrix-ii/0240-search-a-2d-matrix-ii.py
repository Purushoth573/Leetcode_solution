from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        for row in matrix:
            if binarysearch(row, target) != -1:
                return True
        
        return False
