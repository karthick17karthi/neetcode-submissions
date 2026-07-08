class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[]
        for i in range(len(temperatures)):
            n=temperatures[i]
            count=0
            for j in range(i+1,len(temperatures)):
                if(temperatures[j]>n):
                    count=j-i
                    break
            l.append(count)
        return l
