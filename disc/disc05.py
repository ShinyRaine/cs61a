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

def add_this_many(x, el, lst):
  assert type(lst) == list
  i = 0
  while i < x:
    lst.append(el)
    i += 1

def group_by(s, fn):
  res = {}
  for i in s:
    t = fn(i)
    if type(res.get(t)) == list:
      res[t].append(i)
    else:
      res[t] = [i]
  return res

# print(group_by(range(-3, 4), lambda x: x * x))

def partition_options(total, biggest):
  if total == 0:
    return [[]]
  if biggest == 0:
    return []
  if total == 1:
    return [[1]]
  with_biggest = [[biggest] + i for i in partition_options(total - biggest, biggest)]
  without_biggest = partition_options(total, biggest - 1)

  return with_biggest + without_biggest

# print(partition_options(4, 3))

def min_elements(T, lst):
  if T == 0:
    return 0
  return min([1 + min_elements(T - i, lst) for i in lst if T >= i])

print(min_elements(10, [4, 2, 1]))