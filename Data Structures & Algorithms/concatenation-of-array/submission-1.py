class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(n):
            a.append(nums[i])
        for i in range(n):
            a.append(nums[i])
        return a