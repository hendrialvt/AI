import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)
y = 3*x + 4
plt.plot(x,y)
plt.title('Grafik y = 3x + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.show()