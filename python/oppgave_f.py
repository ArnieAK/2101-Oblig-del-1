##DAPE2101 - Oblig del 1 oppgave f
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

avstand = np.sqrt((x_B - x_A)**2 + (y_B - y_A)**2)
plt.plot(t, avstand)
plt.xlabel('t - sekunder')
plt.ylabel('Avstand - meter')

#Når t = T_f
indeks = np.argmin(np.abs(t - T_f)) #For å finne nærmeste indeks
avstand_v_Tf = avstand[indeks]
avstand_avrundet = round(avstand_v_Tf, 2)

#Output
print(f"Avstanden når t = T_f er {avstand_avrundet} meter")
plt.plot(T_f, avstand_v_Tf, 'ro', markersize=7, label='Avstand ved T_f')
plt.legend()
plt.grid()
plt.show()

