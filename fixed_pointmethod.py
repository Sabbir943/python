import math

def f(x):
    return math.sin(x) + math.cos(x) - 1

def g(x):
    return -math.cos(x) / math.sin(x)

def get_inputs():
    while True:
        try:
            a = float(input("Enter the value of a (initial guess): "))
            b = float(input("Enter the value of b: "))
            tolerance = float(input("Enter the tolerance: "))  
            return a, b, tolerance
        except ValueError:
            print("Invalid input, please enter numeric values.")

def fixed_point_iteration(a, b, tolerance):
    x0 = a  
    i = 0
    
    while True:
        x1 = g(x0) 
        relative_error = ((x1 - x0) / x1)  
        print(f"Iteration {i + 1}:")
        print(f"x = {x1}")
        print(f"g(x) = {g(x0)}")
        print(f"Tolerance = {relative_error}\n")
        
        if relative_error < tolerance:
            break
        
        x0 = x1
        i += 1
    
    print(f"Approximate root after {i + 1} iterations: {x1}")

a, b ,tolerance = get_inputs()
fixed_point_iteration(a, b, tolerance)
