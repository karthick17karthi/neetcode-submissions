class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        price=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            price=max(price,prices[i]-mini)
        return price
