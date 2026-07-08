class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr=s.replace(" ","")
        
        strr=re.sub(r'[^a-zA-Z0-9]','',strr)
        strr=strr.lower()
        rev=strr[::-1]
        return rev==strr
        