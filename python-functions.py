def sum_to (num):
  sum = 0
  for i in range(num+1):
    sum+=i
  return sum

print(sum_to(6)) # returns 21
print(sum_to(10)) # returns 55


def largest(list):
  highest=0
  for num in list:
    if num>highest:
      highest=num
  
  return highest

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231


def occurances(str1, str2):
  return str1.count(str2)

print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))   # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0


def product( *args):
  product = 1
  for arg in args:
    product*=arg
  return product

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0

