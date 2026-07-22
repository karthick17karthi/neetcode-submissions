class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        ans=len(s)
        so=sorted(s)
        j=0
        for i in so:
            nums[j]=i
            j+=1
        return ans