class Solution:
    def validPalindrome(self, s: str) -> bool:
        a=s[::-1]
        if(a==s):
            return True
        for i in range(len(s)):
            v=s[:i]+s[i+1:]
            if(v==v[::-1]):
                return True
        return False