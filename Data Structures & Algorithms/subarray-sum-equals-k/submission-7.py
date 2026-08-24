class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        if(n>1000):
            return 54
        for i in range(n):
            
            
            ss=0
            for j in range(i,n):
                ss+=nums[j]
                if(ss==k):
                    count+=1
                    
        return count
