import math
def f(x):
    return 4*math.e**-x*math.sin(x)-1

def initial_guess():
    while True:
        try:
            a=int(input("Enter first initial guess: "))
            b=int(input("Enter second initial guess: "))
            
            if f(a)*f(b)<0:
                return a,b
            else:
                print("Invalid guess, Plz Enter valid guess")
        
        except:
            print("Invalid input")


def false_position(a,b,tolerance):
    previous_c=None
    i=0
    while True:
        
        c=((a*f(b)-b*f(a))/(f(b)-f(a)))
        print("Iteration ",i + 1,": c = ",c," f(c) = ",f(c))
         
        if previous_c is not None and ((c-previous_c)/c)<=tolerance:
            break
        
        previous_c = c
        
        if f(a) * f(c) < 0:  
            b = c
        else:  
            a = c
        i += 1
    print("Approximate root after ",i+1," iterations: ",c)
      
tolerance = 0.05
a,b=initial_guess()
false_position(a,b,tolerance)
