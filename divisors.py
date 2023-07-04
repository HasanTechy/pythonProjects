def calculate_divisors(number):
    divisors = []

    for i in range(1, (number//2)+1):
        if number % i == 0:
            divisors.append(i)

    return divisors

# Ask the user for input
number = int(input("Enter a number: "))

# Calculate the divisors
divisors = calculate_divisors(number)

# Display the divisors
print("Divisors of", number, "are:")
for divisor in divisors:
    print(divisor)
print(number)
