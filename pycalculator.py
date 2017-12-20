''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''
operators = ['+', '-', '*', '/']

# This function adds two numbers 
def add(x, y):
    return x + y

# This function subtracts two numbers 
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1. For Addition- Enter '+'")
print("2. For Subtraction- Enter '-'")
print("3. For Multiplication- Enter '*'")
print("4. For Division- Enter '/'")

# Take input from the user
choice = input("Enter choice( '+'/ '-'/ '*'/ '/'):")

def checkOperator(choice):
    if choice in operators:
        print("Valid Operator entered!")
    else:
        print("Invalid Operator entered")

checkOperator(choice)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))



if choice == '+':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '/':
    if num2 == 0:
        print("num2 cannot be zero")
    else:
        print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")