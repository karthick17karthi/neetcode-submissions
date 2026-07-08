class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        d={}
        s=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for key,values in d.items():
            if(values>n//3):
                s.append(key)
        return s
            
