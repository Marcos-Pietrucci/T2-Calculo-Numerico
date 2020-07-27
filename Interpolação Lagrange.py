import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import curve_fit

'''
O codigo da Interpolação de Lagrange e seus graficos foram modificados da seguinte fonte:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html
'''

#Funcao do enunciado
def f(x):
    return 1.0/(1.0 + 25.0*x*x)

x_k = np.linspace(2, 28, 26) #Vetor contendo o valor para k utilizados em cada iteracao 
e_k = [] #Vetor para armazenar o erro maximo para determinado k de x_k[], correspondendo a k+1 pontos 
xOriginal = np.linspace(-1.0, 1.0, 1000) #Recurso usado para impressao das funcoes

#Calculo do erro maximo para i = k+1 pontos utilizados
for i in range(3, 29, 1):

    yOriginal = f(xOriginal)

    #Gerando pontos igualmente espacados e seus respectivos valores em f(x)
    xPontos = np.linspace(-1.0, 1.0, i)
    yPontos = f(xPontos)

    #poly armaneza o polinomio propriamente dito
    poly = lagrange(xPontos,yPontos)

    xInterpolacao = np.linspace(-1.0, 1.0, 1000) #Recurso usado para impressao do polinomio
    yInterpolacao = poly(xInterpolacao)

    #Cálculo do erro
    e_aux = abs(f(xOriginal) - poly(xOriginal))
    e_k.append(float(np.amax(e_aux)))

'''
#Plot do polinomio
plt.plot(xOriginal,yOriginal,label = "Função Original")
plt.plot(xPontos,yPontos,'o',label = "Pontos")
plt.plot(xInterpolacao,yInterpolacao,label = "Polinomio da Interpolação")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.4,1.2)
plt.title('Funcao original e interpolacao por lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()
'''

#Plot do erro
plt.plot(x_k, e_k, label = "Função Erro")
plt.plot(x_k, e_k, 'o', label = "Pontos do Erro")
plt.xlim(0, 32)
plt.ylim(-30, 600)
plt.title('Erro em funcao de k')
plt.xlabel('k')
plt.ylabel('Erro')
plt.legend(loc='upper left')

plt.show()

'''
Com n pontos -> dividimos o intervalo [-1, 1], de tamanho 2, em (n-1) partes.
Assim os pontos distam: 2/(n-1)
'''
#Definindo o formato da funcao que relaciona o erro e a distancia entre os pontos
def errorFunc(h, C, q):
    return C*(h**q)

#Preenchendo vetor que representa a distancia entre os pontos para dado numero de pontos
h = []

for j in range(3, 29, 1):
    h.append(2 / (j-1))

#Usando minimos quadrados para encontrar os parametros C e q
parametros = curve_fit(errorFunc, h, e_k)
[C, q] = parametros[0]

print('\nNa aproximacao Ch^q, temos:','\nC = ', C, '\nq = ', q, '\n')

#Definindo a funcao errorFunc com os parametros corretos 
def error(h):
    return C*(h**q)

x_error = np.linspace(0.05, 1.1, 1000)
y_error = error(x_error)

#Plot dos pontos e da funcao error
plt.plot(h, e_k, 'o', label = 'Pontos do erro')
plt.plot(x_error, y_error, label = 'Curva ajustada por minimos quadrados (Ch^q)')
plt.title('Valor do erro em funcao da distancia entre os pontos')
plt.xlabel('Distancia entre os pontos (h)')
plt.ylabel('Erro')
plt.ylim(-50.0, 600.0)
plt.legend(loc='upper right')
plt.show()