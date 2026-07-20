def positive(num):
    return num >= 0

numbers = [10, -5, 0, 25, -15, 40, -8]

result = list(filter(positive, numbers))

print("Original List :", numbers)
print("After Removing Negative Numbers :", result)
