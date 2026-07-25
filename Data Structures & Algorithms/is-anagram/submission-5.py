class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            s1.append(s[i])
            s2.append(t[i])
        s1.sort()
        s2.sort()
        a1="".join(s1)
        a2="".join(s2)
        return a1==a2