class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        s={}
        for i in strs:
            key=''.join(sorted(i))
            if key in s:
                s[key].append(i)
            else:
                s[key]=[i]
        return list(s.values())