def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    # Start the Fibonacci sequence
    fib = [0, 1]
    
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])  # Sum of last two numbers

    print(fib)  # Ensure the output is in the correct format
