def make_lambda(params, body):
  """
  >>> f = make_lambda("x, y", "x + y")
  >>> f
  <function <lambda> at ...>
  >>> f(1, 2)
  3
  >>> g = make_lambda("a, b, c", "c if a > b else -c")
  >>> g(1, 2, 3)
  -3
  >>> make_lambda("f, x, y", "f(x, y)")(f, 1, 2)
  3
  """
  return eval("lambda " + params + ":" + body)

def make_lambda(params, body):
  return eval(f"lambda {params}: {body}")