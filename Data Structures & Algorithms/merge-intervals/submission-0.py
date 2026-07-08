class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        first=[intervals[0]]
        st=[]
        for i in range(1,len(intervals)):
            
            start=intervals[i][0]
            end=intervals[i][1]
            lastend=first[-1][1]
            if(start<=lastend):
                first[-1][1]=max(end,lastend)
            else:
                first.append([start,end])
        return first


            