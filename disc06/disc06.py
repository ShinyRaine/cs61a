def memory(n):
  def fn(f):
    nonlocal n
    return f(n)
  return fn

def nonlocalist():
  """
  >>> prepend, get = nonlocalist()
  >>> prepend(2)
  >>> prepend(3)
  >>> prepend(4)
  >>> get(0)
  4
  >>> get(1)
  3
  >>> get(2)
  2
  >>> prepend(8)
  >>> get(2)
  3
  """
  get = lambda x: "Index out of range!"
  def prepend(value):
    nonlocal get
    f = get
    def get(i):
      if i == 0:
        return value
      return f(i - 1)

  return prepend, lambda x: get(x)


square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
  """Return a higher-order function that prints its
  memories.
  >>> f = memory(3, lambda x: x)
  >>> f = f(square)
  3
  >>> f = f(double)
  9
  >>> f = f(print)
  6
  >>> f = f(square)
  3
  None
  """
  def g(h):
    nonlocal f, x
    print(f(x))
    return memory(x, h)
  return g

# f = memory(3, lambda x: x)
# f = f(square)
# f = f(double)
# f = f(print)
# f = f(square)

def announce_losses(who, last_score=0):
  """
  >>> f = announce_losses(0)
  >>> f1 = f(10, 0)
  >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
  Oh no! Player 0 just lost 9 point(s).
  >>> f3 = f2(7, 10)
  >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
  >>> f5 = f4(11, 12)
  """
  assert who == 0 or who == 1, 'The who argument should indicate a player.'
  def say(score0, score1):
    if who == 0:
      score = score0
    elif who == 1:
      score = score1
    if score < last_score:
      print('Oh no! Player', who, 'just lost', (last_score - score), 'point(s).')
    return announce_losses(who, score)
  return say

# f = announce_losses(0)
# f1 = f(10, 0)
# f2 = f1(1, 10)
# f3 = f2(7, 10)
# f4 = f3(7, 11)
# f5 = f4(11, 12)
def fox_says(start, middle, end, num):
  """
  >>> fox_says('wa', 'pa', 'pow', 3)
  'wa-pa-pa-pa-pow'
  >>> fox_says('fraka', 'kaka', 'kow', 4)
  'fraka-kaka-kaka-kaka-kaka-kow'
  """
  def repeat(k):
    return '-'.join([middle for i in range(k)])
  return start + '-' + repeat(num) + '-' + end

# print(fox_says('wa', 'pa', 'pow', 3))

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


def primary_stress(t):
  """
  >>> word = tree("", [
  tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),
  tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
  >>> primary_stress(word)
  'so'
  >>> phrase = tree("", [
  tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),
  tree("w", [tree("requirement")])])
  >>> primary_stress(phrase)
  'law'
  """
  def helper(t, num_s):
    if is_leaf(t):
      return [label(t), num_s]
    if label(t) == "s":
      num_s = num_s + 1
    return max([helper(b, num_s) for b in branches(t)], key = lambda x: x[1])
  return helper(t, 0)[0]

# word = tree("", [
#   tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),
#   tree("w", [tree("requirement")])])
# print(primary_stress(word))

def subset_sum(seq, k):
  seq.sort()
  for i in range(len(seq)):
    if (k - seq[i]) in seq[i+1:]:
      return True
    subset_sum(seq[i+1:], k - seq[i])
  return False

print(subset_sum([2, 4, 7, 3], 5))
print(subset_sum([1, 9, 5, 7, 3], 2))
print(subset_sum([1, 1, 5, -1], 3))