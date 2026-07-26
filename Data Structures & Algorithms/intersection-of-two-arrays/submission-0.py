class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        s=set()
        for i in nums1:
            d[i]=d.get(i,0)+1
        for i in range(len(nums2)):
            if(nums2[i] in d):
                s.add(nums2[i])
            else:
                continue
        return list(s)