# https://github.com/Divya0822/COP-Lab
# Partner 1: Divya Singh
# Partner 2: Anabel
import math
def square_root(a):
    if a<0:
        raise ValueError("")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a*b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("")
    return math.log(b,a)
def exp(a, b):
    return a**b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division Error")
    return b/a






