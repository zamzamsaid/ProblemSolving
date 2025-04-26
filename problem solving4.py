#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:




