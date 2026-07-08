class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        s=[]
        c=0
        for i in range(n):
            if(nums[i]!=val):
                s.append(nums[i])
            
        for i in range(len(s)):
            nums[i]=s[i]
        return len(s)