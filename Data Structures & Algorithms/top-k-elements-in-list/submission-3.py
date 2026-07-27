class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        s=set()
        for i in range(k):
            num=0
            ak=0
            for k,val in d.items():
                if(val>num):
                    num=val
                    ak=k
            s.add(ak)
            del d[ak]
        return list(s)



        
            
        
            
