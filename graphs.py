# Librerías
import numpy as np
import matplotlib.pyplot as plt
# Funciones
def sobre_amortiguado(y0,y0p,beta,delta,t):
	return(((np.exp(-beta*t))*0.5)*((y0 + ((y0p + beta*y0)/delta))*np.exp(delta*t) + (y0 - ((y0p + beta*y0)/delta))*np.exp(-delta*t)))
def sub_amortiguado(y0,y0p,beta,delta,t):
	return((np.exp(-beta*t))*(y0*np.cos(delta*t) + ((y0p + beta*y0)/delta)*np.sin(delta*t)))
def critico(y0,y0p,beta,delta,t):
	return((np.exp(-beta*t))*(y0 + (y0p + beta*y0)*t))
# Variables
y0 = 100
y0p = 0
# Gráficos
t = np.linspace(0,10,1000)
zero = np.zeros(1000)
fig, axs = plt.subplots(ncols=1, nrows=1, figsize=(10, 5))
axs.plot(t,sobre_amortiguado(y0,y0p,1,0.5,t), label='Oscilador sobreamortiguado')
axs.plot(t,sub_amortiguado(y0,y0p,0.3,1,t), label='Oscilador subamortiguado')
axs.plot(t,critico(y0,y0p,1,0.1,t), label='Oscilador críticamente amortiguado')
axs.plot(t,zero,":")
axs.set_ylabel('Amplitud')
axs.set_xlabel('Tiempo')
axs.legend()
fig.tight_layout()
plt.show()
