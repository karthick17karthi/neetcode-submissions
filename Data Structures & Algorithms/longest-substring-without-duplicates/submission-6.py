class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0

        for i in range(n):
            sett=set()
            for j in range(i,n):
                if s[j] not in sett:
                    sett.add(s[j])
                else:
                    break
            l=max(l,len(sett))
        return l
            