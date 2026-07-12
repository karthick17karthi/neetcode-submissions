class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if(i!=j):
                    mul=mul*nums[j]
            s.append(mul)
        return s