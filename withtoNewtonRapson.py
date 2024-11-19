import math


def f(x):
    return x**2 - 2  

def df(x):
    return 2 * x  


def get_inputs():
    while True:
        try:
            a = float(input("Enter the first value: "))
            b = float(input("Enter the second value: "))
            if f(a) * f(b) < 0:
                return a, b
            else:
                print("wrong input")
        except ValueError:
            print("try again")


def newton_raphson(a, b):
    x0 = a 
    i = 0

    
    while True:
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            return None

       
        x1 = x0 - fx / dfx

        print(f"Iteration {i + 1}:")
        print(f"x_{i} = {x0}")
        print(f"x_{i+1} = {x1}")
        

        x0 = x1
        i += 1

    print(f"Approximate root after {i + 1} iterations: {x1}")
    return x1


a, b = get_inputs()
newton_raphson(a, b)