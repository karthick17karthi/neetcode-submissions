class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(len(s)):
            
            chset=set()
            for j in range(i,len(s)):
                if s[j] in chset:
                    break
                else:
                    chset.add(s[j])
            l=max(l,len(chset))
        return l
        