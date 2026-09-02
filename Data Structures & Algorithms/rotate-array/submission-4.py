class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(k%n):
            last=nums[n-1]
            for i in range(n-1,-1,-1):
                nums[i]=nums[i-1]
            nums[0]=last
                
