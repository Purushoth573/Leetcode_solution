from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """n = len(prices)
        def f(ind, buy, cap):
            if ind == n or cap == 0:
                return 0

            if buy:
                return max(-prices[ind] + f(ind + 1, 0, cap),
                       0 + f(ind + 1, 1, cap))
            else:
                return max(prices[ind] + f(ind + 1, 1, cap - 1),
                       0 + f(ind + 1, 0, cap))

        return f(0, 1, 2)"""
    
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = min(buy1, price)           # buy first stock
            sell1 = max(sell1,price-buy1)   # sell first stock
            buy2 = min(buy2, price-sell1)    # buy second stock
            sell2 = max(sell2, price-buy2)   # sell second stock

        return sell2
