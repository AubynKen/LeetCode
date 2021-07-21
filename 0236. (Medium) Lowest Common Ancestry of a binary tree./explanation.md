## The solution

```python
def lowestCommonAncestor(self, root, p, q):
  if root in (None, p, q): return root
  left, right = map(lambda node: self.lowestCommonAncestor(node, p, q,), (root.left, root.right))
  return root if left and right else left or right
```

## The expanded solution (for easier understanding)

```python
def lowestCommonAncestor(self, root, p, q):
  # The search function returns the LCA if p and q are in node and its subtrees
  def search(node):
    # edge case
    if node is None:
      return None
    # if the node itself is p or q, it doesn't matter where the other one is, the LCA can only be the node itself
    if node == p or node == q:
      return node
    # now we search in the two sub trees
    left = search(node.left)
    right = search(node.right)
    # There are three cases:
    # if the node has one of (p, q) in the left subtree and another one in the right subtree, then the node itself is the LCA
    # notice that search(node) returns a non-null value only if the tree rooted at node contains p or q
    if left and right:
      return node
    # else, if one of them returns a non-null value, that's the LCA
    if left:
      return left
    if right:
      return right
    # if we can't find anything in either of the two subtrees, then the LCA isn't found
    return None
```

