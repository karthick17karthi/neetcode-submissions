class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(x**0.5)
        if(x==0):
            return 0
        ans=1
        for i in range(1,x+1):
            if i*i>x:
                return ans
            ans=i
        return ans