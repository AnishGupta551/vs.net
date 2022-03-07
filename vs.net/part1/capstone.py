# calculator app: this app can add, subtract, multiply, divide, and find the square root of numbers
import math


def addition(num):
  result = 0
  for i in range(int(num)):
    if (i==0):
      num_to_add = int(input("What is the first number to you want to add?"))
      result = result+num_to_add
    else:
      num_to_add = int(input("What is the next number you want to add?"))
      result = result+num_to_add

  print(result)

def subtraction(num):
  result = 0
  for i in range(num):
    if (i==0):
      num_to_subtract = int(input("What is the first number to you want to subtract?"))
      result = num_to_subtract
    else:
      num_to_subtract = int(input("What is the next number you want to subtract?"))
      result = result-num_to_subtract

  print(result)

def multiplication(num):
  result = 0
  for i in range(num):
    if (i==0):
      num_to_multiply = int(input("What is the first number to you want to multiply?"))
      result = result*num_to_multiply
    else:
      num_to_add = int(input("What is the next number you want to multiply?"))
      result = result*num_to_multiply

  print(result)

def division(num):
  result = 0
  for i in range(num):
    if (i==0):
      num_to_divide = int(input("What is the first number to you want to divide?"))
      result = result/num_to_divide
    else:
      num_to_add = int(input("What is the next number you want to divide?"))
      result = result/num_to_divide

  print(result)
  
def square_root():
    number = int(input("Enter the number you would like to find the square root of: "))
    sqrt = math.sqrt(number)
    print(sqrt)
    
def square():
    number = int(input("Enter the number you would like to square: "))
    print(number*number)

print("Welcome to the calculator!")
print()

while (True):
  operation = input("To add numbers, press 1. To subtract numbers, press 2. To multiply numbers, press 3. To divide numbers, press 4. To find the square root of a number, press 5:")
  if (operation == "1"):
    how_many_numbers = input("How many numbers would you like to add?")
    addition(how_many_numbers)
  elif (operation == "2"):
    how_many_numbers = input("How many numbers would you like to subtract?")
    subtraction(how_many_numbers)
  elif (operation == "3"):
    how_many_numbers = input("How many numbers would you like to multiply?")
    multiplication(how_many_numbers)
  elif (operation == "4"):
    how_many_numbers = input("How many numbers would you like to divide?")
    division(how_many_numbers)
  elif (operation=='5'):
    square_root(number)
  else:
    print('That was not a valid input')
    operation = input("To add numbers, press 1. To subtract numbers, press 2. To multiply numbers, press 3. To divide numbers, press 4. To find the square root of a number, press 5:")