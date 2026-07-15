# Program to keep only numbers greater than 15

numbers = [5,10,15,20,25,30]

greater_numbers = []

for i in numbers:
    if i > 15:
        greater_numbers.append(i)

print("Original List:", numbers)
print("Numbers greater than 15:", greater_numbers)
