def generate_subsets():
  """
  >>> subsets = generate_subsets()
  >>> for _ in range(3):
  ... print(next(subsets))
  ...
  [[]]
  [[], [1]]
  [[], [1], [2], [1, 2]]
  """
  i = 0
  subset = [[]]
  while True:
    yield subset
    i += 1
    subset += [s + [i] for s in subset
    
]
# subsets = generate_subsets()
# for _ in range(3):
#   print(next(subsets))

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

def sum_paths_gen(t):
  """
  >>> t1 = tree(5)
  >>> next(sum_paths_gen(t1))
  5
  >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
  >>> sorted(sum_paths_gen(t2))
  [6, 7, 10]
  """
  if is_leaf(t):
    yield label(t)
  for b in branches(t):
    for s in sum_paths_gen(b):
      yield label(t) + s

# t1 = tree(5)
# print(next(sum_paths_gen(t1)))
# t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
# print(sorted(sum_paths_gen(t2)))

class Student:
  students = 0 # this is a class attribute
  def __init__(self, name, ta):
    self.name = name # this is an instance attribute
    self.understanding = 0
    Student.students += 1
    print("There are now", Student.students, "students")
    ta.add_student(self)
  def visit_office_hours(self, staff):
    staff.assist(self)
    print("Thanks, " + staff.name)

class Professor:
  def __init__(self, name):
    self.name = name
    self.students = {}
  def add_student(self, student):
    self.students[student.name] = student
  def assist(self, student):
    student.understanding += 1


class Email:
  """Every email object has 3 instance attributes: the
  message, the sender name, and the recipient name.
  """
  def __init__(self, msg, sender_name, recipient_name):
    self.message = msg
    self.sender_name = sender_name
    self.recipient_name = recipient_name

class Server:
  """Each Server has an instance attribute clients, which
  is a dictionary that associates client names with
  client objects.
  """
  def __init__(self):
    self.clients = {}
  def send(self, email):
    """Take an email and put it in the inbox of the client
    it is addressed to.
    """
    self.clients[email.recipinent_name].inbox.append(email)

  def register_client(self, client, client_name):
    """Takes a client object and client_name and adds them
    to the clients instance attribute.
    """
    self.clients[client_name] = client

class Client:
  """Every Client has instance attributes name (which is
  used for addressing emails to the client), server
  (which is used to send emails out to other clients), and
  inbox (a list of all emails the client has received).
  """
  def __init__(self, server, name):
    self.inbox = []
    self.server = server
    self.name = name
  def compose(self, msg, recipient_name):
    """Send an email with the given message msg to the
    given recipient client.
    """
    email = Email(msg, self.name, recipient_name)
    self.server.send(email)
  def receive(self, email):
    """Take an email and add it to the inbox of this
    client.
    """
    self.inbox.append(email)


class Pet():
  def __init__(self, name, owner):
    self.is_alive = True # It's alive!!!
    self.name = name
    self.owner = owner
  def eat(self, thing):
    print(self.name + " ate a " + str(thing) + "!")
  def talk(self):
    print(self.name)

class Cat(Pet):
  def __init__(self, name, owner, lives=9):
    self.is_alive = True # It's alive!!!
    self.name = name
    self.owner = owner
    self.lives = lives

  def talk(self):
    """ Print out a cat's greeting.
    >>> Cat('Thomas', 'Tammy').talk()
    Thomas says meow!
    """
    print(self.name, 'says meo!')
  def lose_life(self):
    """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
    becomes False. If this is called after lives has reached zero, print out
    that the cat has no more lives to lose.
    """
    if self.is_alive:
      self.lives -= 1
      if self.lives == 0:
        self.is_alive = False
    else:
      print(self.name, 'has no more lives to lose')

class NoisyCat(Cat): # Fill me in!
  """A Cat that repeats things twice."""
  def talk(self):
    """Talks twice as much as a regular cat.
    >>> NoisyCat('Magic', 'James').talk()
    Magic says meow!
    Magic says meow!
    """
    Cat.talk(self)
    Cat.talk(self)

