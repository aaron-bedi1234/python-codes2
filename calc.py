def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("fuction calculator")
try:
    a = float(input("first number: "))
    b = float(input("second number: "))
    op = input("operation (add, subtract, multiply, divide): ")
    if op == "add":
        print("result:", add(a, b))
    elif op == "subtract":
        print("result:", subtract(a, b))
    elif op == "multiply":
        print("result:", multiply(a, b))
    elif op == "divide":
        print("result:", divide(a, b))
    else:
        print("unknown operation.")
except ValueError:
    print("please type numbers only.")
except ZeroDivisionError:
    print("you cannot divide by zero.")
finally:
    print("thanks for using the calculator!")