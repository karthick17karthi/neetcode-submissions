class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        
        for i in range(k%l):
            last=nums[-1]
            for j in range(l-1,0,-1):
                nums[j]=nums[j-1]
            nums[0]=last
        
                
