class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=1
        while True:
            flag=True
            for i in nums:
                if m==i:
                    flag=False
                    break
            if flag:
                return m
            else:
                m+=1

