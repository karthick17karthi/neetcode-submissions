class Solution:
    def validPalindrome(self, s: str) -> bool:
        rev=s[::-1]
        if(rev==s):
            return True
        for i in range(len(s)):
            ans=s[:i]+s[i+1:]
            if ans==ans[::-1]:
                return True
        return False