class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=s.split()
        a=st[-1]
        return len(a)