y = "y"
h = y
def y(y):
  h = "h"
  if y == h:
    return y + "i"
  y = lambda y: y(h)
  return lambda h: y(h)
# y = y(y)(y)

def keep_ints(cond, n):
  """Print out all integers 1..i..n where cond(i) is true
  >>> def is_even(x):
  ... # Even numbers have remainder 0 when divided by 2.
  ... return x % 2 == 0
  >>> keep_ints(is_even, 5)
  2
  4
  """
  i = 1
  while i <= n:
    if cond(i):
      print(i)
    i += 1

def is_even(x):
  # Even numbers have remainder 0 when divided by 2.
  return x % 2 == 0
# keep_ints(is_even, 5)

def make_keeper(n):
  def f(cond):
    i = 1
    while i <= n:
      if cond(i):
        print(i)
      i += 1
  return f


def is_even(x):
  # Even numbers have remainder 0 when divided by 2.
  return x % 2 == 0
# make_keeper(5)(is_even)

def print_delayed(x):
  """Return a new function. This new function, when called,
  will print out x and return another function with the same
  behavior.
  >>> f = print_delayed(1)
  >>> f = f(2)
  1
  >>> f = f(3)
  2
  >>> f = f(4)(5)
  3
  4
  >>> f("hi")
  5
  <function print_delayed> # a function is returned
  """
  def delay_print(y):
    # nonlocal x
    print(x)
    # x = y
    return print_delayed(y)
  return delay_print

def print_n(n):
  """
  >>> f = print_n(2)
  >>> f = f("hi")
  hi
  >>> f = f("hello")
  hello
  >>> f = f("bye")
  done
  >>> g = print_n(1)
  >>> g("first")("second")("third")
  first
  done
  done
  <function inner_print>
  """
  def inner_print(x):
    if n <= 0:
      print("done")
    else:
      print(x)
    return print_n(n - 1)
  return inner_print

f = print_n(2)
f = f("hi")
f = f("hello")
f = f("bye")
g = print_n(1)
g("first")("second")("third")

def remove(n, digit):
  kept, digits = 0, 0
  while n > 0:
    n, last = n // 10, n % 10
    if last != digit:
      kept += last * digits * 10
      digits += 1
  return kept