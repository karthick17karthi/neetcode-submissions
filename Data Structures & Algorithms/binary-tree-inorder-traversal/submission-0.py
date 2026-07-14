# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def in_order(karthi):
            if not karthi:
                return
            in_order(karthi.left)
            ans.append(karthi.val)
            in_order(karthi.right)
        in_order(root)
        return ans
