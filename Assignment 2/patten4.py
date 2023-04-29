from math import factorial

n = int(input("Enter the number of rows: "))

# Initialize the triangle with the first row
triangle = [[1]]

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i) // (factorial(j) * factorial(i-j)),end=" ")
    print()

n = 5

# Loop through each row
for i in range(n):
    # Print the spaces before the numbers
    print("  "*(n-i-1), end="")
    # Loop through each column in the row
    for j in range(i+1):
        # Print the numbers in sequence
        print(j+1, end=" ")
    # Move to the next line after each row
    print()


n = 5

# Loop through each row
for i in range(n):
    # Print the spaces before the asterisks
    print("  "*(n-i-1), end="")
    # Loop through each column in the row
    for j in range(2*i+1):
        # Print the asterisks in a pyramid shape
        print("*", end=" ")
    # Move to the next line after each row
    print()
