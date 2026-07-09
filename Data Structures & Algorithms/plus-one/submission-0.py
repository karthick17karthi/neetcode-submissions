class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in range(len(digits)):
            s+=str(digits[i])
        d=int(s)
        tot=d+1
        string=str(tot)
        ans=[]
        for i in range(len(string)):
            ans.append(int(string[i]))
        return ans