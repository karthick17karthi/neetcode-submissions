class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ind=-1
        for i in range(n):
            if(nums[i]==target):
                ind=i
                break
            elif(nums[i]<target):
                continue
            elif(nums[i]>target):
                ind=i
                break
        return n if ind==-1 else ind