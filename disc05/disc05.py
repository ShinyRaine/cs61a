def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def height(tree):
  """Returns the height of a tree"""
  if is_leaf(tree):
    return 1
  return max([height(t) for t in branches(tree)])

def square_tree(t):
  """Return a tree with the square of every element in t"""
  val = label(t) * label(t)
  if is_leaf(t):
    return tree(val, [])
  return tree(val, [square_tree(i) for i in branches(t)])


def find_path(tree, x, l = []):
  if label(tree) == x:
    return l + [x]
  if is_leaf(tree):
    return None
  for t in branches(tree):
    path = find_path(t, x, l + [label(tree)])
    if path != None:
      return path
  return None
# t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
# print(find_path(t, 5))
# print(find_path(t, 10))
