class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=""
        n=len(s)
        for i in range(n-1,-1,-1):
            
            st+=(s[i])
        for i in range(len(st)):
            s[i]=st[i]

