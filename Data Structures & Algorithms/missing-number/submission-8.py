class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        miss=-1
        for i in range(n):
            if(nums[i]!=i):
                miss=i
                return i
            else:
                continue
        return n
