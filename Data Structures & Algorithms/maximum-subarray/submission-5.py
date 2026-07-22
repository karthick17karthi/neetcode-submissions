class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f=nums[0]
        maxx=nums[0]
        for i in range(1,len(nums)):
            f=max(nums[i],f+nums[i])
            maxx=max(maxx,f)
        return maxx

            