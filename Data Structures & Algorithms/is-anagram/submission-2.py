class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=[]
        c2=[]
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            c1.append(s[i])
            c2.append(t[i])
        c1.sort()
        c2.sort()
        b=False
        for i in range(len(s)):
            if(c1[i]==c2[i]):
                b=True
            else:
                b=False
                break
        return b

        