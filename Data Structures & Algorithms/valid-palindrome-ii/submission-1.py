class Solution:
    def validPalindrome(self, s: str) -> bool:
        rev=s[::-1]
        if(rev==s):
            return True
        for i in range(len(s)):
            e=s[:i]+s[i+1:]
            if(e==e[::-1]):
                return True
        return False