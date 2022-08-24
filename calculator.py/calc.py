import os 
from ascii import logo

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multipy(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": substract,
    "*": multipy,
    "/": divide
}
def calc():
    print(logo)

    num1 = float(input("Insert the 1st number : "))
    for symbol in operations:
        print(symbol)
    should_cont = True
    while should_cont:
        op_symbol = input("What you want to do ? ")
        num2 = float(input("Insert the next number : "))
        calc_function = operations[op_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating {answer} or 'n' to start the new calculation type 'exit' to exit: ") == "y":
            num1 = answer
            os.system('cls')
        else:
            should_cont = False
            calc()
            os.system('cls')

calc()