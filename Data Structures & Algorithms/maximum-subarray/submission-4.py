class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ka=nums[0]
        maxx=nums[0]
        for i in range(1,len(nums)):
            ka=max(nums[i],ka+nums[i])
            maxx=max(maxx,ka)
        return maxx
            