class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            so=''.join(sorted(i))
            if so in d:
                d[so].append(i)
            else:
                d[so]=[i]
            
        return list(d.values())


        