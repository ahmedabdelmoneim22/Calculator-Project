from art import logo
print(logo)
def CALCULATE_operator(num1,operator,num2):
    if operator=="+":
        num1+=num2
    elif operator=="-":
        num1-=num2
    elif operator=="*":
        num1*=num2
    elif operator=="/":
        num1/=num2
    else:
        return "Error operator."
    return num1
################################
def CALCULATE():
    finish_Calculate=True
    num1=float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    while finish_Calculate:
        operator=str(input("Pick an operation: "))
        num2=float(input("What's the next number?: "))
        num3=CALCULATE_operator(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {num3}")
        num1=num3
        continue_calc=str(input(f"Type 'y' to continue calculating with {num1}, "
                                f"or type 'n' to start a new calculation: "))
        if continue_calc=='n':
            finish_Calculate=False
#$$$$$$$The_infinity_Loop$$$$$$$$.
while True:
    CALCULATE()
    A = input("Continue or End: ")
    if A == "End":
        break

#############
#This for Me.
#Not popular to use it in software Engineering:
#1)recursion c++(Not popular).
#2)pointer c++(Not popular).
#3)memory allocation c++(Not popular).
#4)N-version programming(popular).
###############
