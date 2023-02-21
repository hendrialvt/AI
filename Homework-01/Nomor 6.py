import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y1 = 3*x + 4
y2 = 2*x**2 + 1
y3 = x**3 + 3

plt.plot(x,y1,'r', label='y = 3x + 4')
plt.plot(x,y2,'g', label='y = 2x^2 + 1')
plt.plot(x,y3,'b', label='y = x^3 + 3')

plt.title('Grafik Tugas 6')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()