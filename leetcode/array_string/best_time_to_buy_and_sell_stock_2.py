from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profits = []
        for i in range(len(prices)-1):
            if prices[i] >= prices[i+1]:
                continue
            else:
                profits.append(prices[i+1] - prices[i])
        
        if profits:
            answer = sum(profits)
        else:
            answer = 0

        return answer
        
        