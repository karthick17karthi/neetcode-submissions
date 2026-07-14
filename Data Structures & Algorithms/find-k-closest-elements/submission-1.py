class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s = []

        for i in range(len(arr)):
            diff = abs(arr[i] - x)
            s.append((diff, arr[i]))

        s.sort()

        ans = []

        for i in range(k):
            ans.append(s[i][1])

        ans.sort()

        return ans