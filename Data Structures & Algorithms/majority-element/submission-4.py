class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        k=-1
        m=-1
        for key,values in d.items():
            if(values>m):
                m=values
                k=key
        return k

    