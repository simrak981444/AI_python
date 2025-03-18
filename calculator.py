import math
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def division (x,y):
    if y==0:
        return "error"
    else:
        return x/y
def floor_divide(x, y):
    return x // y
def ceiling_divide(x, y):
    return math.ceil(x / y)
def calculator():
   x = float(input("Enter first number: "))
   y = float(input("Enter second number: "))
   print(f"{x} + {y} = {add(x, y)}")
   print(f"{x} - {y} = {subtract(x, y)}")
   print(f"{x} * {y} = {multiply(x, y)}")
   print(f"{x} / {y} = {division(x, y)}")
   print(f"{x} / {y} = {floor_divide(x, y)}")
   print(f"{x} / {y} = {ceiling_divide(x, y)}")
   calculator()



