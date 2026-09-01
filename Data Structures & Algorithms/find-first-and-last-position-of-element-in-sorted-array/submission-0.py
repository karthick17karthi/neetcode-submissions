class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count=0
        ind=-1
        ans=[]
        n=len(nums)
        for i in range(n):
            if(nums[i]==target):
                count+=1
                ind=i

                if(count==1):
                    ans.append(i)
            
        if(count>=1):
            ans.append(ind)
        if not ans:
            return [-1,-1]
        return ans
            