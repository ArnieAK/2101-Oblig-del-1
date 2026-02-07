##DAPE2101 - Oblig del 1 oppgave a og b
import numpy as np


#Forskjellige verdier
a = 9.81 
R = 20
w = np.sqrt(a/R)
w_avrundet = round(w, 2)
h = 1.5
u = 6 #Starthastighet - radiell
r = R-h
v = r * w #Tangentiell
#v og u står vinkelrett på hverandre - kan bruke Pythagoras
vBall = np.sqrt(v**2 + u**2)
vBall_avrundet = round(vBall, 2)

print(f"Oppgave a: vinkelhastigheten er {w_avrundet} radianer/sekundet")
print(f"Oppgave b: hastigheten til ballen er {vBall_avrundet} meter/sekundet")

