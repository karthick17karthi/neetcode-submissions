class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        for i in range(n):
            ss=set()
            for j in range(i,n):
                if s[j] not in ss:
                    ss.add(s[j])
                else:
                    break
            l=max(l,len(ss))
        return l


     
            