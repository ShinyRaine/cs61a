def is_prime(n):
  """
  >>> is_prime(10)
  False
  >>> is_prime(7)
  True
  """
  i = 2
  res = True
  while i < n:
    if n % i == 0:
      res = False
    i += 1
  return res

is_prime(10)