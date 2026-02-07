##DAPE2101 - Oblig del 1 oppgave e
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

x_A_f = R * np.cos(w*T_f - pi/2)
y_A_f = R * np.sin(w*T_f - pi/2)
x_B_f = v* T_f
y_B_f = (h-R) + u * T_f

#Beregning for astronauten
r_A = R * np.ones(len(t))
theta_A = w*t - pi/2
#Beregning for ball
r_B = np.sqrt(x_B**2 + y_B**2)
theta_B = np.arctan2(y_B, x_B)

#Posisjoner ved T_f
theta_A_f = w*T_f - pi/2
r_A_f = R
theta_B_f = np.arctan2(y_B_f, x_B_f)
r_B_f = np.sqrt(x_B_f**2 + y_B_f**2)

#Plot i r,theta planet
plt.plot(theta_A, r_A, label='Astronaut')
plt.plot(theta_B, r_B, label='Ball')
plt.plot(theta_A_f, r_A_f, 'ro', markersize = 7, label = 'A når t=T_f')
plt.plot(theta_B_f, r_B_f, 'bo', markersize = 7, label = 'B når t_T_f')
plt.xlabel('θ - radianer')
plt.ylabel('r - meter')
plt.legend()
plt.grid()
plt.show()