class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        s=[]
        used=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in range(k):
            kk=-1
            fre=-1
            for keys,values in d.items():
                if(values>fre and keys not in used):
                    fre=values
                    kk=keys
            s.append(kk)
            used.append(kk)
        return s