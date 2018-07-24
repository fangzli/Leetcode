# Method 1: recursive, slow, no memory of previously calculated value
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(5))

# Method 2: iterative
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# Method 3: recursive, fast, has memory of prev calc value
memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
# print(fibm(5))

# 1. Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3
def mul3(n):
    if n == 1:
        return 3
    else:
        return 3 + mul3(n-1)
# print mul3(3)

# 2. Write a recursive Python function that returns the sum of the first n integers.
# (Hint: The function will be similiar to the factorial function!)
def sumn(n):
    if n == 0:
        return 0
    else:
        return n + sumn(n-1)
# print sumn(6)

# 3. Write a function which implements the Pascal's triangle:
# 1
# 1    1
# 1    2    1
# 1    3    3    1
# 1    4    6    4    1
# 1    5    10    10    5    1
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        pre_line = pascal(n-1)
        for i in range(len(pre_line) - 1):
            line.append(pre_line[i] + pre_line[i+1])
        line.append(1)
        return line
#print pascal(6)

# 4. You find further exercises on our Python3 version of recursive functions,
# e.g. creating the Fibonacci numbers out of Pascal's triangle or produce
# the prime numbers recursively, using the Sieve of Eratosthenes.

