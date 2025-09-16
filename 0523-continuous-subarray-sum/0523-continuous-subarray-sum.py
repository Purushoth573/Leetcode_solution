class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixsum=0
        hashmap={}
        hashmap[0]=-1
        for i, n in enumerate(nums):
            prefixsum+=n
            rem=prefixsum%k
            rem=(rem+k)%k # to avoid negative number
            if rem not in hashmap:
                hashmap[rem]=i
            elif i-hashmap[rem]>1:
                return True
        return False
        