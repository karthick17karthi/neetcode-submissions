class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[]
        count=0
        k=2
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for k,v in d.items():
            if v>=1:
                for i in range(min(2,v)):
                    arr.append(k)
        for i in range(len(arr)):
            nums[i]=arr[i]
        return len(arr)


            
