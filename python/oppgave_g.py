##DAPE2101 - Oblig del 1 oppgave g
import numpy as np
import matplotlib.pyplot as plt
#Forskjellige verdier
a = 9.81 
R = 20
w = np.sqrt(a/R)
h = 1.5
u = 6
r = R-h
v = r * w 
pi = np.pi
#tid
t_start = 0
t_slutt = 10
t = np.linspace(t_start, t_slutt, 1000)
#Astronaut
x_A = R * np.cos(w*t - pi/2)
y_A = R * np.sin(w*t - pi/2)
#Ball
x_B = v * t
y_B = (h-R) + u * t
#fra oppgave d
a_d = v**2 + u**2
b_d = 2* (h-R) * u
c_d = (h-R)**2 - R**2
løsning_d = np.roots([a_d, b_d, c_d])
T_f = round(løsning_d[0], 2)

#Theta for astronauten
theta_A = w*t - pi/2

x_A_prim = 0
y_A_prim = 0

x_B_prim = -np.sin(theta_A) * (x_B - x_A) + np.cos(theta_A) * (y_B - y_A)
y_B_prim = -np.cos(theta_A) * (x_B - x_A) - np.sin(theta_A) * (y_B - y_A)


#Når t = T_f
indeks = np.argmin(np.abs(t - T_f)) #For å finne nærmeste indeks

x_B_prim_f = x_B_prim[indeks]
y_B_prim_f = y_B_prim[indeks]

#Plot
plt.plot(x_B_prim_f, y_B_prim_f, 'ro', markersize=7, label='B ved T_f')
plt.plot(x_B_prim, y_B_prim, label='Ball')
plt.plot(x_A_prim, y_A_prim, 'go', markersize=7, label='Astronaut')
plt.xlabel("x' (m)")
plt.ylabel("y' (m)")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()

