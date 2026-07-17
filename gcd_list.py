#program to find the GDC of all number in a list
numbers = [24, 36, 48, 60]

smallest = min(numbers)

gcd = 1

for i in range(1, smallest + 1):
    divisible = True

    for num in numbers:
        if num % i != 0:
            divisible = False
            break

    if divisible:
        gcd = i

print("Numbers :", numbers)
print("GCD :", gcd)
