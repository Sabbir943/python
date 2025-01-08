def f(x):
    return x**3 - x -1

def initial_guess():
    while True:
        try:
            a=int(input("Enter first initial guess: "))
            b=int(input("Enter second initial guess: "))
            
            if f(a)*f(b)<0:
                tolerance=float(input("Enter tolerance in % : "))
                return a, b, tolerance
            
            else:
                print("Invalid Guess, Please enter right guess")
        
        except:
            print("Invalid Input")

def bisection(a,b,tolerance):
    prev_c=0
    
    i=0
    while True:
        c=(a+b)/2
        print("Iteration: ",i+1,"c = ",c,"f(c) = ",f(c))
        
        if c != 0 and abs(((c - prev_c)/c)*100)<=tolerance:
            break
        prev_c=c
        
        if f(a) * f(c) < 0:
            b=c
        else:
            a=c
        i += 1
    print("Approximate Root after ",i+1,"iteration is : ",c)

a,b,tolerance=initial_guess()
False_Position(a,b,tolerance)