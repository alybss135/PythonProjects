# type code here for fibonacci iteration
def fibonacci_iteration(n):
    
    # the start of the sequence 
    sequence = [0, 1]

    if (n <= 0):
        return n
    
    if (n > 1):
        for i in range(n - 2):
            sequence.append((sequence[i] + sequence[i + 1]))

    return sequence

#print(fibonacci_iteration(-1))
#print(fibonacci_iteration(0))
#print(fibonacci_iteration(1))
#print(fibonacci_iteration(5))
#print(fibonacci_iteration(6))

def fibonacci_recursion(n):
    sequence = []

    if (n <= 0):
        return n
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursion(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

print(fibonacci_recursion(-2))
print(fibonacci_recursion(0))
print(fibonacci_recursion(1))
print(fibonacci_recursion(2))
print(fibonacci_recursion(5))
print(fibonacci_recursion(7))