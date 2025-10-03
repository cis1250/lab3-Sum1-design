#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


# prompt + validate a positive integer
while True:
    user_input = input("Enter the number of Fibonacci terms: ").strip()
    if user_input.isdigit() and int(user_input) > 0:
        n = int(user_input)
        break
    print("Please enter a positive integer.")

# generate + print
a, b = 0, 1
for i in range(n):
    print(a, end=" " if i < n - 1 else "\n")
    a, b = b, a + b


