class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ans=-1
        nums.sort()
        for i in range(n):
            if(i!=nums[i]):
                return i
        return n
