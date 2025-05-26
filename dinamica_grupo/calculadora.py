
def soma(a, b):
    return a + b

def mult(a, b):
    return a * b

def sub(a, b):
    return a -b

def div(a, b):
    return a / b

def square_sum(a ,b):
    return (a + b) ** 2

def execute_op(a, b, func):
    return func(a, b)


print(execute_op(2, 3, soma))
print(execute_op(2, 3, mult))
print(execute_op(2, 3, sub))
print(execute_op(2, 3, div))
print(execute_op(2, 3, div))
print(execute_op(2, 3, square_sum))