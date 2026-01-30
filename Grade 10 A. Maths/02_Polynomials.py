import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 400)
a, b = 3, 2
x = a * np.cos(t)
y = b * np.sin(t)

plt.plot(x, y)
plt.axis('equal')
plt.show()