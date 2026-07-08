class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=[]
        for i in nums1:
            s.append(i)
        for i in nums2:
            s.append(i)
        s.sort()
        n=len(s)
        if(len(s)%2!=0):
            return s[len(s)//2]
        else:
            return (s[n // 2] + s[n // 2 - 1]) / 2