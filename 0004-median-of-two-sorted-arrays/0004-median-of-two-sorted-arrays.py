class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2
        
        l, r = 0, n - 1
        while True:
            i = (l + r) // 2  # partition in nums1
            j = half - i - 2  # partition in nums2

            # Handle edges safely
            aleft  = nums1[i] if i >= 0 else float("-inf")
            aright = nums1[i+1] if i+1 < n else float("inf")
            bleft  = nums2[j] if j >= 0 else float("-inf")
            bright = nums2[j+1] if j+1 < m else float("inf")

            # Partition is correct
            if aleft <= bright and bleft <= aright:
                # Odd
                if total % 2:
                    return min(aright, bright)
                # Even
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1
