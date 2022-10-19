def main():
  print(multiplication(6,-10))
  print(exponentiation(-2,3))
  print(square(5))

def multiplication(x,y):
  result=0
  for i in range (abs(y)):
    result=result+x
  if y<0:
    result=0-result
  return result

def exponentiation(x,y):
  result=1
  for i in range (y):
    result=result*x
  return result

def square(x):
  return (exponentiation(x,2))


main()