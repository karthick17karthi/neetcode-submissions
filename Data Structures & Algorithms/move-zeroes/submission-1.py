class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        for i in range(len(nums)):
            if(nums[i]!=0):
                a.append(nums[i])
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j]=a[j]
                j+=1
        while(j<len(nums)):
            nums[j]=0
            j+=1
