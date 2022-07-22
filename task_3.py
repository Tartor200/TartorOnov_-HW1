num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
op = input("Enter the operation: ")

if op == "mod":
    op = "%"
elif op == "pow":
    op = "**"
elif op == "div":
    op = "//"
    
#eval = evaluate...
if num2 == "0" and (op == "/" or "//" or "%"):
    print("Division by zero!")
else:
    print(eval(num1+op+num2))
