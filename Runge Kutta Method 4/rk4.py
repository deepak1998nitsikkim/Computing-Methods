def rkm(x,y):
    return x+y
    
x0 = 0
y0 = 1

x = 0.2
y = y0
n=int(input("enter the amount of iterations : "))
h = (x - x0)/n

for i in range(1,n+1):
    k1 = h*rkm(x0,y0)
    k2 = h*rkm(x0+h/2, y0+k1/2)
    k3 = h*rkm(x0+h/2,y0+k2/2)
    k4 = h*rkm(x0+h,y0+k3)
    
    y += (k1+2*k2+2*k3+k4)/6
    print(round(y,4))