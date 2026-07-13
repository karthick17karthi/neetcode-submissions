class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1=len(word1)
        s2=len(word2)
        t=s1
        ans=""
        i=0
        j=0
        while(i<s1 and j<s2):
            ans+=word1[i]
            i+=1 
            ans+=word2[j]
            j+=1
        ans+=word1[i:]
        ans+=word2[j:]
        return ans 
           