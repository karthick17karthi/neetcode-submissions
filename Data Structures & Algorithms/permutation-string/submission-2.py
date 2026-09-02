class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ak=sorted(s1)
        n=len(s1)
        for i in range(len(s2)-n+1):
            ans=sorted(s2[i:i+n])
            if(ans==ak):
                return True
        return False