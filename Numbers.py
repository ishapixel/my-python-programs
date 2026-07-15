#from functools import reduce

# List of numbers
numbers = [2,5,7,8,9,10,11]

# Step 1: Keep only odd numbers
odd = list(filter(lambda x:x % 2 !=0, numbers))
print("Odd numbers:", odd)

# Step 2: Double the odd numbers
double = list(map(lambda x:x * 2, odd))
print("Doubled numbers:", double)

# Step 3: Subtract all numbers one by one
result = reduce(lambda a, b: a - b, double)

print("Final Result:", result)
