import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y1 = x**2-1
y2 = 3*x+3
plt.plot(x, y1, 'b', x,y2,'r')
plt.grid()

plt.title("Graph of y1 and y2")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('y1=x^2-1','t2=3*x+3'))
plt.show()