class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub):
            return sub == sub[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try skipping either the left or the right character
                return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
            l += 1
            r -= 1
        return True
