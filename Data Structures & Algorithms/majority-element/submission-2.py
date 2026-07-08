class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        ind=0
        if n==1:
            return nums[0]
        for i in range(n-1):
            c=0
            for j in range(i+1,n):
                
                if(nums[i]==nums[j]):
                    c+=1
                else:
                    continue
            if c>count:
                count=c
                ind=nums[i]
        return ind
    