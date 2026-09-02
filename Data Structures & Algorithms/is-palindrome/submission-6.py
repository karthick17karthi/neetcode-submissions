class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        st=''
        for i in s:
            if i.isalnum():
                st+=i.lower()
        return st==st[::-1]
"""

        
        ss=s.replace(" ","")
        ss=re.sub(r'[^a-zA-Z0-9]','',ss)
        ss=ss.lower()
        return ss==ss[::-1]
        
        