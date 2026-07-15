# Program to sort numbers based on their last digit

numbers = [13, 38, 42, 27, 65, 81]
result = sorted(numbers, key=lambda num: num % 10)

print("Original List :", numbers)
print("Sorted List :", result)
