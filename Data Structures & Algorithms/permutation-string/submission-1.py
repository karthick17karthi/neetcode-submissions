class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ak=sorted(s1)
        k=len(s1)
        for i in range(len(s2)-k+1):
            s=sorted(s2[i:i+k])
            if(s==ak):
                return True
        return False