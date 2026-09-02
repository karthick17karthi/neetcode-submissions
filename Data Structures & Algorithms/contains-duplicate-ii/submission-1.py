class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        count=0
        s=set()
        for i in nums:
            
            if i in s:
                
                return True
            else:
                s.add(i)
            if count>=k:
                s.remove(nums[count-k])
            count+=1
        return False
