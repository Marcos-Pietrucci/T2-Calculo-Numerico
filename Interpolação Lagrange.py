import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial



def f(x):
    return 1.0/(1.0 + 25*x*x)

xOriginal = np.linspace(-1, 1,1000) 
yOriginal = f(xOriginal)


xPontos = np.linspace(-1, 1,20) 
yPontos = f(xPontos)

poly = lagrange(xPontos,yPontos)


xInterpolacao = np.linspace(-1, 1,1000) 
yInterpolacao = poly(xInterpolacao)


plt.plot(xOriginal,yOriginal,label = "Função Original")
plt.plot(xPontos,yPontos,'o',label = "Pontos")
plt.plot(xInterpolacao,yInterpolacao,label = "Função Interpolação")
plt.legend(loc='upper left') 
plt.ylim((-0.4,1.2))

plt.show() 