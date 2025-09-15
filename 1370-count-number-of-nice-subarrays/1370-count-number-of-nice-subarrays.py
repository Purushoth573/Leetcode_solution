class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr=[1 if x%2  else 0 for x in nums]
        print(arr)
        res=0
        prefixsum={0:1}
        cursum=0
        for i in arr:
            cursum+=i
            if cursum-k in prefixsum:
                res+=prefixsum[cursum-k]
            if cursum in prefixsum:
                prefixsum[cursum]+=1
            else:
                prefixsum[cursum]=1
        return res

        