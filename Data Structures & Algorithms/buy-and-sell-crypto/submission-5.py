class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float('inf')
        pro=0
        for i in prices:
            minn=min(minn,i)
            pro=max(pro,i-minn)
        return pro
        