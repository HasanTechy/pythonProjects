def generate_fibonacci(n):
    fibonacci_numbers = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers

# Ask the user for input
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate the Fibonacci numbers
fibonacci_sequence = generate_fibonacci(n)

# Print the Fibonacci numbers
print("Fibonacci sequence:")
for number in fibonacci_sequence:
    print(number)
