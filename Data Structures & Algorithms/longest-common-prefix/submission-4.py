class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        ans=""
        for i in range(1,len(strs)):
            temp=""
            j=0
            k=0
            second=strs[i]
            while(j<len(first) and k<len(strs[i])):
                if(first[j]==second[k]):
                    temp+=second[k]
                else:
                    break
                j+=1
                k+=1

            
            first=temp
        return first