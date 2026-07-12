class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st=''
        for i in s:
            if i.isalnum():
                st+=i.lower()
        return st==st[::-1]


        """ st=s.replace(" ","")
        st=re.sub(r'[^a-zA-Z0-9]','',st)
        st=st.lower()
        rev=st[::-1]
        return st==rev"""
        