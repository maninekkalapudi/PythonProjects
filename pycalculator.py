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

choice = ""

def checkOperator():
    # Take input from the user
    global choice
    choice = input("Enter choice( '+'/ '-'/ '*'/ '/'):")

# Check the operator 
    if choice in operators:
        print("Valid Operator entered")
        print("Choice: ",choice)
        return True
    else:
        print("Invalid Operator entered!")
        return False


while checkOperator() is False:
    checkOperator()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(choice)

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