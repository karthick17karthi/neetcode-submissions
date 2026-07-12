class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        ans=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for key,val in d.items():
            if(val>n//2):
                ans=key
        return ans

    