import numpy as nupy
import matplotlib.pyplot as plt

# crear una figura de 8 x 6 puntos especificos (points),
# usando 100 puntos por pulgada (dpi)
plt.figure(figsize=(8,6), dpi=80)

# crear un subgráfica
plt.subplot(111)

# creamos un conjunto de datos de -PI a +PI
# entre esos dos tenemos 256 valores
X = nupy.linspace(-nupy.pi,nupy.pi,256,endpoint=True)

# creamos los valores de salida para las Funciones
# seno y coseno , con respecto a los valores de entrada
# de "X"

C, S = nupy.cos(X), nupy.sin(X)

# gráficamos la función coseno
# con los siguiente atributos

# pagina de colores https://www.rapidtables.com/web/color/RGB_Color.html
plt.plot(X, C, color="blue", linewidth=3.5, linestyle='-', label='coseno')

# gráficamos la función seno
# con los siguiente atributos

#cambio de color
plt.plot(X, S, color="red", linewidth=3.5, linestyle='-', label='seno')

# ponemos donde queremos mostrar la leyenda
plt.legend(loc='upper left', frameon=True)

# limitamos el eje "x"
plt.xlim(X.min()*1.1, X.max()*1.1)

#limitamos el eje "y"
plt.ylim(C.min()*1.1, C.max()*1.1)

# definimos una marca de referencia para el eje
# "x" tanto inicial como final
plt.xticks([-nupy.pi, -nupy.pi/2, 0, nupy.pi/2, nupy.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# definimos una marca de referencia para el eje
# "y" tanto inicial como final

plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

# establecemos la intesección de las líneas de los ejes
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# damos estilo a las marcas de notación para que sean más visibles
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(30)
    label.set_bbox(dict(facecolor='#ffffff', edgecolor='None', alpha=0.65 ))
# graficar un punto en ambas Funciones
# se elige el valor de punto a graficar
t = 2*nupy.pi/3
# graficamos el punto en la función coseno con los siguientes atributos
plt.plot([t,t],[0,nupy.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[nupy.cos(t),], 50, color ='blue')
# Damos notación al punto en la función coseno con formato de latex
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, nupy.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#graficamos el punto en la función seno con los siguientes atributos
plt.plot([t,t],[0,nupy.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[nupy.sin(t),], 50, color ='red')
# Damos notación al punto en la función seno con formato de latex
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, nupy.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# notación de latex en conjunto de parametros de matplotlib
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.annotate
# https://matplotlib.org/users/annotations_guide.html

# guardar gráfica con calidad de
# 80 pixeles por pulgada
plt.savefig("matplotlib_test_9.png",dpi=80)

# mostramos la gráfica creada
plt.show()
