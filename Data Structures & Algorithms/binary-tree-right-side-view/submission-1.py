# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        bfs = []
        q = deque([])
        q.append(root)

        while q:
            # level = []
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    # level.append(node.val)
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                
            # if level:
                # bfs.append(level)
            if rightSide:
                bfs.append(rightSide.val)
        # return [l[-1] for l in bfs]
        return bfs
        