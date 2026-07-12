class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans=[]
        for i in nums1:
            if(i!=0):
                ans.append(i)
        for j in nums2:
            if(j!=0):
                ans.append(j)
        for i in range(len(ans)):
            nums1[i]=ans[i]
        nums1.sort()

        