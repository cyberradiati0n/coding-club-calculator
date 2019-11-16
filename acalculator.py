print("Welcome to my calculator program!")
num1 = int(input("Which is the first number you wish to use?"))
num2 = int(input("Which is the second number you wish to use?"))
operation = input("Which operation would you like to use?")

def add():
  sum1 = num1 + num2
  print(sum1)

def multiply():
  prod1 = num1 * num2
  print(prod1)
  
def divide():
  quo1 = num1 / num2
  print(quo1)
  
def subtract():
  diff1 = num1-num2
  print(diff1)
  
if operation == "add":
  add()

if operation == "subtract":
    subtract()

if operation == "multiply":
  multiply()

if operation == "divide":
  divide()

