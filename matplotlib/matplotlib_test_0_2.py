import matplotlib.pyplot as plt
import numpy as nupy

# evenly sampled time at 200ms intervals
t = nupy.linspace(0.,1.,50,endpoint=True)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
