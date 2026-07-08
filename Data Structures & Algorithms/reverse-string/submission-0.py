class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        ans=[]
        for i in range(n-1,-1,-1):
            ans.append(s[i])
        ii=0
        for i in ans:
            s[ii]=i
            ii+=1