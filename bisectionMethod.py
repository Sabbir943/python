def f(x):
    return x**3+x**2+x+7

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


def Bisection_Method(a,b,max_iteration):
    previous_c=None
    for i in range(max_iteration):
        
        c=(a+b)/2
        print("Iteration ",i + 1,": c = ",c," f(c) = ",f(c))
         
        if previous_c is not None and abs(c - previous_c) ==0:
            break
        
        previous_c = c
        
        if f(a) * f(c) < 0:  
            b = c
        else:  
            a = c
    
    print("Approximate root after ",i+1," iterations: ",c)
      

a,b=initial_guess()
Bisection_Method(a,b,100)