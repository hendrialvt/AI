import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = 2*x**2 + 1
plt.plot(x,y)
plt.title('Grafik y = 2x^2 + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()