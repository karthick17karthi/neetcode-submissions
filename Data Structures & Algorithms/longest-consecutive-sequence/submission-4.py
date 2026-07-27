class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s=list(sorted(set(nums)))
        
        if not s:
            return 0
        count=1
        long=1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]+1):
                count+=1
            else:
                long=max(long,count)
                count=1
        long=max(long,count)
        return long
