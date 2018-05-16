import matplotlib.pyplot as plt
import numpy as nupy
def f(t):
    return nupy.exp(-t) * nupy.cos(2*nupy.pi*t)

t1 = nupy.arange(0.0, 5.0, 0.1)
t2 = nupy.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, nupy.cos(2*nupy.pi*t2), 'r--')
plt.show()

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot
