class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """l,r=0,1
        max_profit=0
        while r< len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_profit=max(max_profit,profit)
            else:
                l=r
            r+=1
        return max_profit"""
        n = len(prices)
        @lru_cache(None)
        def f(ind, buy, cap):
            if ind == n or cap == 0:
                return 0

            if buy:
                # either buy at this index OR skip
                return max(-prices[ind] + f(ind + 1, 0, cap),
                       f(ind + 1, 1, cap))
            else:
            # either sell at this index OR skip
                return max(prices[ind] + f(ind + 1, 1, cap - 1),
                       f(ind + 1, 0, cap))

        return f(0, 1, 1)