class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i + 1, n):
                hashset = set()
                for k in range(j + 1, n):
                    sum_ = nums[i] + nums[j] + nums[k]
                    fourth = target - sum_
                    if fourth in hashset:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))  # Tuples are hashable for set
                    hashset.add(nums[k])
        ans = [list(t) for t in st]
        return ans
        