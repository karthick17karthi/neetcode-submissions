class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        
        for i in nums:
            s.add(i)
        so=sorted(s)
        ind=0
        for i in so:
            nums[ind]=i
            ind+=1
        
        return len(s)