from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # O(N^2) brute force (commented)
        """
        res = 0
        for l in range(len(nums)):
            subarraysum = 0
            for r in range(l, len(nums)):
                subarraysum += nums[r]
                if subarraysum % k == 0:
                    res += 1
        return res
        """

        # O(N) optimized with prefix sums and a normal dict
        prefixsum = 0
        prefix_cnt = {}     # Use a regular dict
        prefix_cnt[0] = 1   # Initialize count for remainder 0
        res = 0

        for n in nums:
            prefixsum += n
            rem = prefixsum % k
            rem = (rem + k) % k  # Ensure non-negative remainder

            # Get the current count for this remainder (default to 0 if not present)
            count = prefix_cnt.get(rem, 0)
            res += count   # Add all previous occurrences
            prefix_cnt[rem] = count + 1  # Update or set to count+1

        return res
