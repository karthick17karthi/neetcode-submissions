class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        st=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if(sum==target):
                    st.append(i)
                    st.append(j)
        return st

        