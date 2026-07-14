# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def post(kk):
            if not kk:
                return
            post(kk.left)
            post(kk.right)
            ans.append(kk.val)
        post(root)
        return ans