def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


operators = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : division
}

def calculator():
    should_accumulate = True

    num1 =  int(input("type the first num: \n"))
    while should_accumulate:

        for symbol in operators:
            print(symbol)
        operation_symbol = input("choose an operation symbol: \n")
        num2 = int(input("type the second num: \n"))

        answer = operators[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2}  =  {answer}")

        conti = input(f"Continue calculate with the {answer}: type y ")

        if conti == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()