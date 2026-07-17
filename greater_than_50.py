#program to find the index of the first number greater than 50
numbers = [12, 35, 48, 51, 72, 90]

for i in range(len(numbers)):
    if numbers[i] > 50:
        print("Index of first number greater than 50 is:", i)
        break
else:
    print("No number greater than 50 found.")
