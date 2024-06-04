def factorial_iteration(n):
    sum = 1
    if (n == 0):
        sum = 1

    if (n > 0):
        for i in range(n):
            sum *= n - i    
    return sum

def factorial_recursion(n):
    sum = 1
    if (n == 0):
        sum = 1
    
    if (n >= 1):
       sum = n * factorial_iteration(n-1)

    return sum

print(factorial_recursion(0))
print(factorial_recursion(1))
print(factorial_recursion(5))