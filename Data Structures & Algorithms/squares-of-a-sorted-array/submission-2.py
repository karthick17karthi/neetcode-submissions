class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            ak=i*i
            a.append(ak)
        a.sort()
        return a
