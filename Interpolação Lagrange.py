import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

'''
O codigo da Interpolação de Lagrange e seus graficos foram modificados da seguinte fonte:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html
'''

def f(x):
    return 1.0/(1.0 + 25.0*x*x)

x_k = np.linspace(3, 29, 26)
e = []
xOriginal = np.linspace(-1.0, 1.0, 1000)

for i in range(3, 29, 1):

    yOriginal = f(xOriginal)

    xPontos = np.linspace(-1.0, 1.0, i)
    yPontos = f(xPontos)

    poly = lagrange(xPontos,yPontos)

    xInterpolacao = np.linspace(-1.0, 1.0, 1000) 
    yInterpolacao = poly(xInterpolacao)

    #Cálculo do erro
    e_aux = abs(f(xOriginal) - poly(xOriginal))
    e.append(float(np.amax(e_aux)))

plt.plot(xOriginal,yOriginal,label = "Função Original")
plt.plot(xPontos,yPontos,'o',label = "Pontos")

plt.plot(xInterpolacao,yInterpolacao,label = "Polinomio da Interpolação")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.4,1.2)
plt.legend(loc='upper left')

plt.show()

plt.plot(x_k, e, label = "Função Erro")
plt.plot(x_k, e, 'o', label = "Pontos do Erro")
plt.xlim(0, 32)
plt.ylim(-30, 600)
plt.legend(loc='upper left')

plt.show()
