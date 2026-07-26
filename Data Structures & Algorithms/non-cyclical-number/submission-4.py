class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        temp=n
        b=True
        while(b):
            summ=0

            while(temp>0):
                last=temp%10
                sq=last*last
                summ+=sq
                temp=temp//10
            temp=summ
            
            if summ in l:
                b=False
                return False
            if summ==1:
                return True
            else:
                l.add(summ)
        return True
