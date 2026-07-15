# List of numbers
numbers = [10,15,18,20,25,27,30]

# Step 1: Filter numbers divisible by 5
divisible = list(filter(lambda x:x % 5 == 0, numbers))

print("Numbers divisible by 5:", divisible)

# Step 2: Find the average
average = sum(divisible) / len(divisible)

print("Average:",average)
