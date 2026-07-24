class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):
            sec=ord(s[i+1])
            first=ord(s[i])
            ans+=abs(sec-first)
        return ans