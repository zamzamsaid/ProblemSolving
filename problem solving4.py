#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Step 1: Ask for the size of the matrix (n x n)
n = int(input("Enter the size of the matrix (n): "))

# Step 2: Create an empty matrix
matrix = []

print("Enter the matrix row by row:")

# Step 3: Take user input for each row
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)#matrix.append(row) adds the row into the matrix.

# Step 4: Initialize diagonal sums
left_to_right = 0
right_to_left = 0

# Step 5: Loop to calculate both diagonal sums
for i in range(n):
    left_to_right += matrix[i][i]# this is the main diagonal (top-left to bottom-right).
    right_to_left += matrix[i][n - 1 - i] #Row i, column n-1-i → this is the other diagonal (top-right to bottom-left).

# Step 6: Calculate absolute difference
difference = abs(left_to_right - right_to_left)

# Step 7: Print the result
print("Absolute difference between diagonals is:", difference)

#map(int-> turns each string into an integer.
# list-> converts the mapped result into a list of numbers (e.g., [1, 2, 3]).


# In[9]:


n = int(input("Enter the size of the matrix (n): "))

matrix = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

left_to_right = 0
right_to_left = 0

for i in range(n):
    left_to_right += matrix[i][i]
    right_to_left += matrix[i][n - 1 - i]

difference = abs(left_to_right - right_to_left)
print("Absolute difference between diagonals is:", difference)

