class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        ind=0
        for i in s:
            nums[ind]=i
            ind+=1
        
        return len(s)