# n = int(input("Enter the number of rows: "))

# # Initialize the triangle with the first row
# triangle = [[1]]

# # Loop through each row up to the nth row
# for i in range(1, n):
#     # Initialize the row with the first element
#     row = [1]
#     # Loop through each column in the row
#     for j in range(1, i):
#         # Calculate the value using the formula (i-1,j) + (i-1,j-1)
#         value = triangle[i-1][j] + triangle[i-1][j-1]
#         # Append the value to the row
#         row.append(value)
#     # Append 1 to the end of the row
#     row.append(1)
#     # Append the row to the triangle
#     triangle.append(row)

# # Print the triangle
# for row in triangle:
#     for element in row:
#         print(element, end=" ")
#     print()


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
