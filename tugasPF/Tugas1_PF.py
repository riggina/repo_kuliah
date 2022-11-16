
#List Comprehensions dan Map
def sum_square(n):
  number_map = list(map(int, str(n)))
  # print(number_map)
  return sum (x * x for x in number_map)
print(sum_square(123))



#Recursion
def triangular(n):
  # for i in range(1,n+1):
    if 1 < n:
      # print(n)
      return n + triangular(n - 1)
    else:
      return 1
print(triangular(5))



#Square generator
def square(num,sqr):
  if num >= 1:
    for i in range(1,sqr):
      num *= num     
    return num
  else:
    print("hanya bilangan bulat positif")
print(square(3,2))



#Palindrome with comparisons
def is_palindrome(text):
  length = len(text)
  for i in range(0, length // 2):
    if(text[i] != text[length -i-1]):
      return False
      
  return True
print(is_palindrome("rotator"))
