from operator import truediv


def multiply(m, n):
  if n == 1:
    return m
  else:
    return m + multiply(m, n - 1)

# print(multiply(5, 3))

def is_prime(n):
  if n == 1:
    return False
  return prime_helper(n, 2)

def prime_helper(n, i):
  if n == i:
    return True
  elif n % i == 0:
    return False
  else:
    return prime_helper(n, i + 1)

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))

def count_stair_ways(n):
  if n == 1:
    return 1
  if n == 0:
    return 1
  return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
  # if k == 1:
  #   return 1
  if n == 0:
    return 1
  if n < 0:
    return 0
  s, i = 0, k
  while i > 0:
    s += count_k(n - i, k)
    i -= 1
  return s


# print(count_k(3, 1))
# print(count_k(4, 4))
# print(count_k(10, 3))

def even_weighted(s):
  return [i * s[i] for i in range(len(s)) if i % 2 == 0]

x = [1, 2, 3, 4, 5, 6]
# print(even_weighted(x))

def max_product(s):
  if len(s) == 0:
    return 1
  if len(s) == 1:
    return s[0]
  return max(s[0] * max_product(s[2:]), max_product(s[1:]))

# print(max_product([10,3,1,9,2]))
# print(max_product([5,10,5,10,5]))

def check_hole_number(n):
  a = n % 10
  b = n // 10 % 10
  c = n // 100 % 10
  if n // 10 == 0:
    return True
  return check_hole_number(n // 100) and a > b and c > b

# print(check_hole_number(123))
# print(check_hole_number(3241968))
# print(check_hole_number(3245968))

def check_mountain_number(n):

  def helper(n, i):
    a = n % 10
    b = n // 10 % 10
    if n // 10 == 0:
      return True
    if a > b:
      return helper(n // 10, 0)
    if a < b:
      if i == 1:
        return helper(n // 10, 1) 
      return False

    # if i == 1:
    #   if a < b:
    #     return helper(n // 10, 1)
    
    # return a > b and helper(n // 10, 0)

  return helper(n, 1)

# print(check_mountain_number(10))
print(check_mountain_number(103))
print(check_mountain_number(153))
print(check_mountain_number(123456))
print(check_mountain_number(2345986))

