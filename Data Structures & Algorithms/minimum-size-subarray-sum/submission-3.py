class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        minn=float('inf')
        for i in range(len(nums)):
            count=0
            curr=0
            for j in range(i,len(nums)):
                
                curr+=nums[j]
                count+=1
                if(curr>=target):
                    minn=min(minn,count)
                    break
        return 0 if minn==float('inf') else minn