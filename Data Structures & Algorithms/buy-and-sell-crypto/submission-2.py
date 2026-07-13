class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        right = -1
        for i in range(1 , len(prices)):
            if prices[i] > right:
                right = prices[i]
            elif prices[i] < left:
                left = prices[i]
        if left >= right:
            return 0
        else:
            return right - left