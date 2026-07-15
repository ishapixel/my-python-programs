#program to filter perfect squares from a list
numbers=[4,5,9,10,12,16,20]
def perfect_square(num):
  root = int(num ** 0.5)
  return root * root == num
result = list(fliter(perfect_square,numbers))
print("original list :",numbers)
print("perfect squares :",result)
              
