class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
        """nums.sort()  # Sort the array first
        res = []
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                ts=nums[i]+nums[l]+nums[r]
                if ts>0:
                    r-=1
                elif ts<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        return res"""

        """n = len(nums)
        st = set()

        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    st.add(tuple(temp))  # sets need hashable objs; use tuple
                hashset.add(nums[j])

        ans = [list(trip) for trip in st]
        return ans
"""
# Example usage:

