def fahrenheit(temp):
    return (temp * 9/5) + 32

celsius = [0, 20, 30, 40, 100]

fahrenheit_list = list(map(fahrenheit, celsius))

print("Celsius Temperature :", celsius)
print("Fahrenheit Temperature :", fahrenheit_list)
