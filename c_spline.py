import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

'''
O codigo de geracao de splines cubicas e seus graficos foi modificado da seguinte fonte:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html
'''

def f(x):
    return 1.0/(1.0 + 25.0*x*x)

xOriginal = np.linspace(-1.0, 1.0,1000) 
yOriginal = f(xOriginal)

xPontos = np.linspace(-1.0, 1.0, 5)
yPontos = f(xPontos)

cs = CubicSpline(xPontos, yPontos, bc_type='natural')

xcs = np.linspace(-1.0, 1.0,1000) 
ycs = cs(xcs)

plt.plot(xOriginal,yOriginal,label = "Função Original")
plt.plot(xPontos, yPontos,'o',label = "Pontos")
plt.plot(xcs, ycs, label="Spline cubica")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.4, 1.2)
plt.legend(loc='upper left')

plt.show()