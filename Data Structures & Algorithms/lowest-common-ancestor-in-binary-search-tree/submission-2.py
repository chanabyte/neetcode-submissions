# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p == root or q==root:
            return root
        if ((root.left.val == p.val or root.right.val == p.val) and root.val == q.val): 
            return root
        elif ((root.left.val == q.val or root.right.val == q.val) and root.val == p.val): 
            return root
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else: return root
