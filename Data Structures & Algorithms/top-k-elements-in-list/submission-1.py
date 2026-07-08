class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        sett=set()
        for i in range(k):
            
            mx=0
            mm=float('-inf')
            for key,value in d.items():
                if(value>mm):
                    mm=value
                    mx=key
            sett.add(mx)
            del d[mx]
        return list(sett)
            
