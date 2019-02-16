### This is to test Python
import math as m
from aguaclara.play import*
import numpy as np

flow = 2*u.m**3/u.s
radius = 0.2*u.m
Diam = radius*2

#make an array of temperatures in Kelvin
Temp = [273,293,313,333,353,373,393,413,433,453,473]
T = np.array(Temp)
T = T*u.kelvin

#Calculate the Reynolds Number for each Temperature
nu = pc.viscosity_kinematic(T)
Rey = pc.re_pipe(flow,Diam,nu)

#Plot Reynolds number vs Temperature
plt.plot(T,Rey,'.')
plt.title('Reynolds Number vs Temperature')
plt.xlabel('Temperature [K]')
plt.ylabel('Reynolds Number')
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.tight_layout()
plt.savefig('./images/Reynolds_Plot.png')
plt.show()
