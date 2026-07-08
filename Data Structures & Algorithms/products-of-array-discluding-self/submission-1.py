class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            pro=1
            for j in range(len(nums)):
                if(i!=j):
                    pro=pro*nums[j]
                else:
                    continue
            s.append(pro)
        return s