import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit

'''
O codigo de geracao de splines cubicas e seus graficos foi modificado da seguinte fonte:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html
'''
#Funcao do enunciado
def f(x):
    return 1.0/(1.0 + 25.0*x*x)

x_k = np.linspace(2, 28, 26) #Vetor contendo o valor para k utilizados em cada iteracao 
e_k = [] #Vetor para armazenar o erro maximo para determinado k de x_k[], correspondendo a k+1 pontos 
xOriginal = np.linspace(-1.0, 1.0, 1000) #Recurso usado para impressao das funcoes
yOriginal = f(xOriginal)

#Calculo do erro maximo para i = k+1 pontos utilizados

#Splines Naturais
for i in range(3, 29, 1):

    #Gerando pontos igualmente espacados e seus respectivos valores em f(x)
    xPontos = np.linspace(-1.0, 1.0, i) 
    yPontos = f(xPontos)

    #cs armaneza a spline cubica propriamente dita
    cs = CubicSpline(xPontos, yPontos, bc_type='natural')

    xcs = np.linspace(-1.0, 1.0, 1000) #Recurso usado para impressao da spline
    ycs = cs(xcs)

    #Calculo do erro
    e_aux = abs(f(xOriginal) - cs(xOriginal))
    e_k.append(float(np.amax(e_aux)))

'''
#Plot da funcao spline cubica
plt.plot(xOriginal,yOriginal,label = "Função Original")
plt.plot(xPontos, yPontos,'o',label = "Pontos")
plt.plot(xcs, ycs, label="Spline cubica")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.4, 1.2)
plt.title('Funcao original e spline cubica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()
'''

#Plot do erro para spline natural
plt.plot(x_k, e_k, label = "Função Erro")
plt.plot(x_k, e_k, 'o', label = "Pontos do Erro")
plt.title('Erro em funcao de k')
plt.xlabel('k')
plt.ylabel('Erro')
plt.legend(loc='upper right')
plt.xticks(range(0, 32, 2))
plt.show()

#Aproximacao Ch^q para Splines Naturais
'''
Com n pontos -> dividimos o intervalo [-1, 1], de tamanho 2, em (n-1) partes.
Assim os pontos distam: h = 2/(n-1)
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

print('\nNa aproximacao Ch^q para spline natural, temos:','\nC = ', C, '\nq = ', q, '\n')

#Definindo a funcao errorFunc com os parametros corretos 
def error(h):
    return C*(h**q)

x_error = np.linspace(0.05, 1.1, 1000)
y_error = error(x_error)

#Plot dos pontos e da funcao error
plt.plot(h, e_k, 'o', label = 'Pontos do erro')
plt.plot(x_error, y_error, label = 'Curva ajustada por minimos quadrados (Ch^q)')
plt.title('Valor do erro em funcao da distancia entre os pontos (para spline natural)')
plt.xlabel('Distancia entre os pontos (h)')
plt.ylabel('Erro')
plt.legend(loc='upper left')
plt.show()

####### SPLINE COM DERIVADA CONHECIDA NOS EXTREMOS #######
'''
Como f'(-1) = 0.07396 e f'(1) = -0.07396, temos que as novas condicoes de contorno
sao cs''(-1) = 0.07396 e cs''(1) = -0.07396.
'''

#Calculando o erro
e_k_2 = []

for i in range(3, 29, 1):

    #Gerando pontos igualmente espacados e seus respectivos valores em f(x)
    xPontos_2 = np.linspace(-1.0, 1.0, i) 
    yPontos_2 = f(xPontos_2)

    #cs armaneza a spline cubica propriamente dita
    cs2 = CubicSpline(xPontos_2, yPontos_2, bc_type = ((1, 0.07396),(1, -0.07396)))

    #Calculo do erro
    e_aux2 = abs(f(xOriginal) - cs2(xOriginal))
    e_k_2.append(float(np.amax(e_aux2)))

#Aproximacao Ch^q para Splines com Derivada Conhecida nos Extremos

#Usando minimos quadrados para encontrar os parametros C e q
parametros2 = curve_fit(errorFunc, h, e_k_2)
[C2, q2] = parametros2[0]

print('\nNa aproximacao Ch^q para derivada conhecida nos extremos, temos:','\nC = ', C2, '\nq = ', q2, '\n')

#Definindo a funcao errorFunc com os parametros corretos 
def error_2(h):
    return C2*(h**q2)

x_error2 = np.linspace(0.05, 1.1, 1000)
y_error2 = error_2(x_error)

#Plot dos pontos e da funcao error
plt.plot(h, e_k_2, 'o', label = 'Pontos do erro')
plt.plot(x_error2, y_error2, label = 'Curva ajustada por minimos quadrados (Ch^q)')
plt.title('Valor do erro em funcao da distancia entre os pontos (derivada conhecida nos extremos)')
plt.xlabel('Distancia entre os pontos (h)')
plt.ylabel('Erro')
plt.legend(loc='upper left')
plt.show()