# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(res):
                res.append([])          # first time at this depth → new level
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res


# Problem: Binary Tree Level Order Traversal (LeetCode 102)
# Approach: DFS with depth indexing (preorder), collecting values by level
# Time Complexity : O(N)
#     Each node is visited exactly once and appended to its level list.
# Space Complexity : O(H) auxiliary (call stack), where H is tree height; worst-case O(N) for a skewed tree.
#     Output storage is O(N) for all node values across levels.
# Did this code successfully run on LeetCode : Yes (102)
# Any problem you faced while coding this :
#    - Forgetting to create a new list when first reaching a depth (depth == len(res)).
#    - Returning [] instead of [] when root is None (handled here).
#    - Confusion about DFS vs BFS: DFS still works if we pass the current depth and bucket by depth.

