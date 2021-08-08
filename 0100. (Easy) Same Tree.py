class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(np, nq):
            if not (np or nq):
                return True
            if not np or not nq or np.val != nq.val:
                return False
            return helper(np.left, nq.left) and helper(np.right, nq.right)
        return helper(p, q)
                