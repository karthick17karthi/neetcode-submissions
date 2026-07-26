class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=set()
        for i in range(k):
            m=0
            key=0
            for k,v in d.items():
                if(v>m):
                    m=v
                    key=k
            ans.add(key)
            del d[key]
        return list(ans)



        
            
        
            
