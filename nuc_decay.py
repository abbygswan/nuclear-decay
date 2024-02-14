
from pylab import *

import matplotlib.pyplot as plt

def dNdt(lam, N):
	return - lam*N
	
def N_of_t(lam, N_0, t_final, steps):
	delta_t = t_final / steps 
	t = 0.0 
	N = N_0 
	t_list = [ t ] 
	N_list = [ N ] 
	N_ana = [ N ]  

	while (t < t_final): 
		N = N + dNdt(lam,N) * delta_t  
		t = t + delta_t   
		t_list.append(t) 
		N_list.append(N) 
		N_ana.append(N_0 * exp( - lam*t)) 

	plt.plot(t_list,N_list, linestyle= "dashed", color = "green", label = "numerical") #plots the numerically calculated N
	plt.plot(t_list,N_ana, linestyle= "solid", color = "red", label = "analytical") #plots the analytical N
	plt.xlabel('t')
	plt.ylabel('N')
	plt.legend()
	plt.savefig("N_of_t.pdf", dpi=150) 
	plt.show() 