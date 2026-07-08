class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=nums[0]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                maxx=max(maxx,s)
        return maxx