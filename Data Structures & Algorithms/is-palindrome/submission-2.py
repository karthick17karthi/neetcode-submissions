class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.replace(" ","")
        st=re.sub(r'[^a-zA-Z0-9]','',st)
        st=st.lower()
        rev=st[::-1]
        return st==rev
        