class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx=0
        sk=""
        for i in range(len(s)):
            strr=""
            for j in range(i,len(s)):
                strr+=s[j]
                rev=strr[::-1]
                if(rev==strr):
                    if(len(strr)>len(sk)):
                    
                        sk=strr
        return sk