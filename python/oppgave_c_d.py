##DAPE2101 - Oblig del 1 oppgave c og d

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
vBall = np.sqrt(v**2 + u**2)
pi = np.pi

#tid
t_start = 0
t_slutt = 10
t = np.linspace(t_start, t_slutt, 1000)

#Astronaut
x_A = R * np.cos(w*t - pi/2)
y_A = R * np.sin(w*t - pi/2)

#Ball
x_B = 0 + v * t
y_B = (h-R) + u * t
#Oppgave d
#Ballen lander når roten av x_B^2 + y_B = 20
#Bruker abc formelen
a_d = v**2 + u**2
b_d = 2* (h-R) * u
c_d = (h-R)**2 - R**2
løsning_d = np.roots([a_d, b_d, c_d])
T_f = round(løsning_d[0], 2)
print(f"Ballen treffer bakken igjen når t = {T_f} sekunder")

#Posisjoner ved T_f
x_A_f = R * np.cos(w*T_f - pi/2)
y_A_f = R * np.sin(w*T_f - pi/2)
x_B_f = v* T_f
y_B_f = (h-R) + u * T_f

#Plot for oppgave C og D
#Markerer punktene i plottet
plt.plot(x_A_f, y_A_f, 'ro', markersize=7, label='A når t=T_f')
plt.plot(x_B_f, y_B_f, 'bo', markersize=7, label='B når t=T_f')
plt.plot(x_A, y_A, label = 'Astronaut')
plt.plot(x_B, y_B, label = 'Ball')
plt.xlabel('X - meter')
plt.ylabel('Y - meter')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()