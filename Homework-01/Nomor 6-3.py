import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(10000)]
x = np.array(x)
y = x**3 + 3
plt.plot(x,y)
plt.title('Grafik y = x^3 + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()