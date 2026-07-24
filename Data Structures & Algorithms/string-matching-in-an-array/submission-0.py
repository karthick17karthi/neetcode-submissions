class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            st=words[i]
            for j in range(len(words)):
                if(i==j):
                    continue
                if st in words[j]:
                    ans.append(st)
                    break
        return ans