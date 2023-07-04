def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    reversed_strings = " ".join(reversed_words)
    return reversed_strings


# Ask the user for input
user_input = input("Enter a long string containing multiple words: ")

# Reverse the words in the string
reversed_strings = reverse_words(user_input)

# Print the reversed string
print("Reversed string with words:")
print(reversed_strings)
