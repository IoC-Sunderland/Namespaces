# Built-in namespace
print(dir(__builtins__))
print('\n')

# The Global Namespace

## Variable Scope

### 1. Local
x = 'global'

def f():
  x = 'enclosing'

  def g():
    x = 'local'
    print(x)

  g()
f() # Prints 'local'

### 2. Enclosing
x = 'global'

def f():
  x = 'enclosing'

  def g():
    print(x)

  g()
f() # Prints 'enclosing'

### 3. Global
x = 'global'

def f():
  def g():
    print(x)

  g()
f() # Prints 'global'

# 4. Built-in

