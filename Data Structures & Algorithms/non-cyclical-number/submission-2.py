class Solution:
    def isHappy(self, n: int) -> bool:
        ak=n
        l=[]
        while(ak!=1):
            
            nn=ak
            summ=0
            while(nn!=0):
                last=nn%10
                sq=last*last
                summ+=sq
                nn=nn//10
            ak=summ
            
            if summ in l:
                return False
            else:
                l.append(summ)

            summ=0
        return True
