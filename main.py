import matplotlib.pyplot as plt, tabulate
x_val=[];y_val=[];plt_x=[];plt_y=[];Data=[]
def function(x,y):
    return x+y**2

x_val.append('x')
y_val.append('y')
def runge_kutts(x0,y0,xn,n):
    yn=0
    h=(xn-x0)/n
    x_val.append(x0)
    y_val.append(y0)
    for i in range(n):
        k1=h*(function(x0,y0))
        k2=h*(function((x0+h/2),(y0+k1/2)))
        k3=h*(function((x0+h/2),(y0+k2/2)))
        k4=h*(function((x0+h),(y0+k3)))

        k=(k1+2*k2+2*k3+k4)/6
        yn=y0+k
        y0=yn
        x0=x0+h
        x_val.append(x0)
        y_val.append(y0)
        plt_x.append(x0)
        plt_y.append(y0)
    print('y(%f)=%f'%(xn,yn))
    Data.append(x_val)
    Data.append(y_val)

print("Initial Condition: ")
x0=float(input("x0: "))
y0=float(input("y0: "))
print("Calculation point: ")
xn=float(input("xn: "))
print("Interval number: ")
n=int(input("interval: "))
runge_kutts(x0,y0,xn,n)

print(tabulate.tabulate(Data,tablefmt='fancy_grid'))



plt.style.use('seaborn')
plt.title('Runge Kutta Method')
plt.plot(plt_x,plt_y,color='red',marker='o',linewidth=1,markersize=4,label='y value')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
