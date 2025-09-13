class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        maxf = 0   # track max frequency in current window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])  # update most frequent char count

            # shrink window if more than k replacements needed
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # update result after ensuring window is valid
            res = max(res, r - l + 1)

        return res
