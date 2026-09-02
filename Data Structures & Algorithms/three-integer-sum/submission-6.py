class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        s=set()
        nums.sort()
        for i in range(n):
            l=i+1
            r=n-1
            while(l<r):
                t=nums[i]+nums[l]+nums[r]
                if(t==0):
                    s.add(tuple([nums[i],nums[l],nums[r]]))
                    l+=1
                    r-=1
                elif(t>0):
                    r-=1
                else:
                    l+=1
        return list(s)


        