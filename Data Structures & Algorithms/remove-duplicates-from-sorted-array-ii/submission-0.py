class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        ans=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for k,v in d.items():
            if(v>=1):
                for i in range(min(2,v)):
                    ans.append(k)
        for i in range(len(ans)):
            nums[i]=ans[i]
        return len(ans)
