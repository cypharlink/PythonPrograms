print("==============")
print("CALCULATOR APP")
print("==============\n")

def line():
    print("\n------------------------\n")

first_num = input("Number: ")

line()

second_num = input("Number: ")

line()

operator = input("Operator (+, -, *, /): ")

line()

if (operator == "+"):
    sum = int(first_num) + int(second_num)
    print("Sum of two number is: " + str(sum))
elif (operator == "-"):
    sub = int(first_num) - int(second_num)
    print("Substraction of two number is: " + str(sub))
elif (operator == "*"):
    mul = int(first_num) * int(second_num)
    print("Multipication of two number is: " + str(mul))
elif (operator == "/"):
    div = int(first_num) / int(second_num)
    print("Division of two number is: " + str(div))
else:
    print("Type a valid operator")