#program to find the maximum number in the list
numbers = [15, 10, 88, 90, 28, 89, 36]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Original List :", numbers)
print("Maximum Number :", maximum)
