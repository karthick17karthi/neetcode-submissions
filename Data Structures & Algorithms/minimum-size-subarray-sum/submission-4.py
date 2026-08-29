class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        cur=0
        ans=float('inf')
        for i in range(len(nums)):
            cur+=nums[i]
            while(cur>=target):
                ans=min(ans,i-l+1)
                cur-=nums[l]
                l+=1
        return 0 if ans==float('inf') else ans