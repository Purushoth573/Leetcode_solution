class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets = [c.lower() for c in s if c.isalnum()  ] 
        result = "".join(alphabets)
        l,r=0,len(result)-1
        while l<=r:
            if result[l]!=result[r]:
                return False
            l+=1
            r-=1
        return True

        