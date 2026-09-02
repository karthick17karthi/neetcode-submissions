class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        pro=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            pro=max(pro,prices[i]-mini)
        return pro
