class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            
            if(i=='(' or i=='{' or i=='['):
                st.append(i)
            else:

                if(not st):
                    return False
                top=st[-1]
                if(i==')' and top=='(' or i=='}' and top=='{' or i==']' and top=='['):
                    st.pop()
                else:
                    return False
        return len(st)==0

            