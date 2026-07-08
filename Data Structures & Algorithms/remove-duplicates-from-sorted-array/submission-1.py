class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=list(set(nums))
        ii=0
        ans.sort()
        for i in ans:
            nums[ii]=i
            ii+=1
        return len(ans)