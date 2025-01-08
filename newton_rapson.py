def f(x):
    return x**3 - x-1

def f_prime(x):
    return 3*x**2-1

def newton_raphson(a, b, epsilon):
    if f(a) * f(b) >= 0:
        return "Error: f(a) and f(b) must have opposite signs"
    
    x0 = a
    while True:
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1

# User input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
epsilon = float(input("Enter the convergence criteria (epsilon): "))

result = newton_raphson(a, b, epsilon)
print("Approximate root:", result)