def fibonacci(limit):
    prev2 = 0
    prev1 = 1
    print(prev2)
    print(prev1)
    for fib in range(limit):
        newFib = prev2 + prev1
        print(newFib)
        prev2 = prev1
        prev1 = newFib

fibonacci(5)


