import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

'''
O codigo de geracao de splines cubicas e seus graficos foi modificado da seguinte fonte:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html
'''

#Funcao do enunciado
def f(x):
    return 1.0/(1.0 + 25*x*x)

#Gerando pontos igualmente espacados em relacao ao eixo x
#x = np.arange(-1.01, 1.01, 0.5)
x = np.arange(-1.01, 1.01, 0.4)
y = f(x)

#Aplicando spline cubica natural
cs = CubicSpline(x, y, bc_type='natural')

 #Gerando pontos nos quais calcularemos os valores de f(x) e da spline cubica
xs = np.arange(-1.01, 1.01, 0.01)
#xs = np.arange(-1.01, 1.01, 0.001) 

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(xs, f(xs), label='Funcao original')
ax.plot(x, y, 'o', label='Pontos')
ax.plot(xs, cs(xs), label="Spline cubica")
ax.set_xlim(-1.5, 1.5)
ax.legend(loc='upper left')

plt.show()

