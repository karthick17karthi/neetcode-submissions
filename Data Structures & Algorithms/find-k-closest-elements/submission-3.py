class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        s=[]
        ans=[]
        for i in range(len(arr)):
            sub=abs(arr[i]-x)
            s.append((sub,arr[i]))
        s.sort()
        for i in range(k):
            
            vip=s[i][1]
            ans.append(vip)
        ans.sort()
        return ans


                
            
