def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operators = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
    
print(operators["*"](2, 3))