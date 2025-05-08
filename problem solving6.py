#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Step 1: Input house and tree positions
s = int(input("Enter house start position (s): "))
t = int(input("Enter house end position (t): "))
a = int(input("Enter apple tree position (a): "))
b = int(input("Enter orange tree position (b): "))

# Step 2: Input fruit distances
apples = list(map(int, input("Enter apple distances (space separated): ").split()))
oranges = list(map(int, input("Enter orange distances (space separated): ").split()))

# Step 3: Calculate where each fruit lands
apple_positions = [a + d for d in apples]
orange_positions = [b + d for d in oranges]

# Step 4: Count fruits that land on the house
apples_on_house = sum(s <= pos <= t for pos in apple_positions)
oranges_on_house = sum(s <= pos <= t for pos in orange_positions)

# Step 5: Print the result
print(f"Apples on house: {apples_on_house}")
print(f"Oranges on house: {oranges_on_house}")

