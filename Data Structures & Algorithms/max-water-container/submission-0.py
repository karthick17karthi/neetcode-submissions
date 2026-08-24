class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=float('-inf')
        l=0
        r=len(heights)-1
        while(l<r):
            w=r-l
            sh=min(heights[r],heights[l])
            area=sh*w
            ans=max(ans,area)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
        return ans

