class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ak=i*i
            ans.append(ak)
        ans.sort()
        return ans
