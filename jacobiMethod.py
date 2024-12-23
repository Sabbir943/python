f1=lambda x,y,z:(17-y+2*z)/20
f2=lambda x,y,z:(-18-3*x+z)/20
f3=lambda x,y,z:(25-2*x+3*y)/20

x0,y0,z0=0,0,0
count=1
n=int(input('Enter the number of iterations:'))

print('\nCount\tx\ty\tz\n')

for _ in range(n):
    x1=f1(x0,y0,z0)
    y1=f2(x0,y0,z0)
    z1=f3(x0,y0,z0)
    
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count,x1,y1,z1))
    
    count+=1
    x0,y0,z0=x1,y1,z1

print('\nSolution after %d iteration: x=%0.3f, y=%0.3f, z=%0.3f\n' % (n,x1,y1,z1))    