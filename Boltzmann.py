

M =  raw_input('Massa (em u.m.a.):')
T =  input ('temperatura (em K):')

UMA = 1.66112e-27


m  = float(M)*UMA
kb = 1.38064852e-23
pi = 3.1415
e  = 2.7182818284590452353602874713527 

m   =  float(m  )
kb  =  float(kb )
pi  =  float(pi )
e   =  float(e  )



K = (m/(2*pi*kb*T)) #constant
print K



def f_ux (ux):
	""" Function doc """
	f_u = (K**0.5) * e **(-m*(ux**2)/(2*kb*T))
	return f_u


def F_u (u):
	""" Function doc """
	F_u = 4*pi * (K**(3.0/2.0)) * e **(-m*(u**2)/(2*kb*T)) * u**2  
	return F_u







print ('Massa molecular     (uma): ', M)
print ('Temperatura         (K)  : ', T)
print ('Massa por particula (kg) : ', m)
print ('Constante                : ', K)


def plot_f_ux (ux_min = 6000 , ux_max = 6000 , step = 1):
	""" Function doc """

	for ux in range(ux_min, ux_max,step):
		f_u = f_ux(ux)
		
		print ux, f_u


#def plot_F_u (u_min = 0 , u_max = 10000 , step = 1):
#	""" Function doc """
u_min = 0 
u_max = 10000
step = 1
soma  =  0.00
for u in range(u_min, u_max, step):
	f_u = F_u (u)
	soma += f_u
	print u, f_u
		
print 'soma', soma
#plot_f_ux ()

