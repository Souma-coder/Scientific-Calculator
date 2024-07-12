# this function adds two numbers and returns the result
def add(num1, num2):
    return num1 + num2

# this function returns the difference between two numbers
def sub(num1, num2):
    return num1 - num2

# this function returns the product of two numbers
def mul(num1, num2):
    return num1 * num2

# this function divides number 1 from number 2 and gives the result 
def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Divide by zero is not possible try again")

# this function returns the percentage of the value
def percent(n):
    return n/100