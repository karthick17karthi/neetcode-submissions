class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        q=[]
        for i in range(len(t)):
            q.append(t[i])
        for i in range(len(s)):
            
            a.append(s[i])
        a.sort()
        q.sort()
        ak="".join(a)
        am="".join(q)
        if(ak==am):
            return True
        return False