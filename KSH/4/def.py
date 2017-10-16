# python "/Users/gimseonghun/Desktop/study-python/KSH/4/def.py"
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
print(fib2(10)) # < 10

def f(a, L=[]): # 
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4))

def t(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(t(1))
print(t(1))
print(t(1))
print(t(1))