import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math as m
import find_x as chi
class Measure:
    def __init__(self , measure:str) -> None:
        self.measure = measure.replace("," , ".").split("±")
        self.inc = float(self.measure[1])
        self.m = float(self.measure[0])

class Point:
    def __init__(self , x ,y , name , dist_x , dist_y):
        self.x_measure = Measure(x)
        self.y_measure = Measure(y)
        self.x = self.x_measure.m
        self.y = self.y_measure.m
        self.inc_x = self.x_measure.inc
        self.inc_y = self.y_measure.inc
        self.name = name
        self.dist_x = dist_x
        self.dist_y = dist_y

#variabili
a = 0
#points
#r1 = Point("10±2","97,80±0,04" ,"r1" , 0 , -5)
#r2 = Point("7±2", "55,50±0,04","r2",0 , -10)
#r3 = Point("7±2","62,20±0,04" ,"r3",0 , 5)
#c1 = Point("9±2","76,42±0,04" ,"c1",0 , -5)
#c2 = Point("11±2", "101,37±0,04","c2",0 , 5)
#c3 = Point("20±2", "184,05±0,04","c3",0 , 10)
r1 = Point("11,5	±	0,2","97,99	±	0,01", "r1" , 0 , -10)
r2 = Point("6,8	±	0,1","55,56	±	0,01" ,"r2"  ,0 , -8)
r3 = Point("7,2	±	0,1" ,"62,31	±	0,01","r3" , 0 , 8)
c1 = Point("4,7	±	0,1" ,"76,57	±	0,01","c1" , 0 ,5 )
c2 = Point("11	±	0,2" ,"101,51	±	0,01","c2",0 , 5)
c3 = Point("23	±	0,2","184,14	±	0,01" ,"c3" , 0 , -8)
#funzione matematica
def math_function(coeff , dati_x):
    f_fit = lambda x: coeff*x
    look_up_table = {dato.x:dato.inc_x for dato in dati}
    retta_fit_x = np.arange(0 , max(dati_x)+look_up_table[max(dati_x)] , 0.001)
    retta_fit_y = list(map(f_fit , retta_fit_x))
    return retta_fit_x , retta_fit_y

#dati = [[11.5,97.99],[6.8,55.56],[7.2,62.31],[4.7,76.57],[11,101.51],[23,184.14]]
dati = [r1 , r2 , r3 , c1 , c2 , c3]
dati_x = [h.x for h in dati]
dati_y = [h.y for h in dati]
inc_x_0 = [h.inc_x for h in dati]
inc_y = [h.inc_y for h in dati]
fig, ax = plt.subplots()
ax.grid(color='lightgray',linestyle='--')
ax.plot(dati_x , dati_y , 'b.' , label="valore medio dato")
for count in range(len(dati_x)):
    x = dati_x[count]
    y = dati_y[count]
    width = inc_x_0[count]*2
    height = inc_y[count]*2
    if(not a):
        ellipse = Ellipse((x,y) , width , height , fill=False , color="c",label="incertezza dato")
        a = 1
    else:
        ellipse = Ellipse((x,y) , width , height , fill=False , color="c")
    ax.add_artist(ellipse)
#coeff = chi.find(dati_x , dati_y , inc_y)
#valori_fit = math_function(coeff[0] , dati_x)
coeff_inv = chi.find(dati_y , dati_x , inc_x_0)
if coeff_inv[1] <= 10: #perchè così si può fare la semidispersione e la media
    coeff_inv = chi.find_m(dati_y , dati_x , inc_x_0 , 10 , coeff_inv[0])
valori_fit_inv = math_function(1/coeff_inv[0] , dati_x)
valori_media_pesata = math_function(9.10 , dati_x)
plt.plot(valori_media_pesata[0],valori_media_pesata[1] , "r"  ,label="retta della media pesata")
#plt.plot(valori_fit[0] , valori_fit[1] , '--g' , label="retta del migliore χ²")
plt.plot(valori_fit_inv[0] , valori_fit_inv[1] , '--' , label="retta del migliore χ² invertito" , color='#808000')
#variabile algoritmo
look_up_table = {}
for dato in dati:
    if dato.inc_y in look_up_table:
        look_up_table[dato.inc_y] = min([look_up_table[dato.inc_y] , dato.y])
    else:
        look_up_table[dato.inc_y] = dato.y

threshold = 0.15
#algoritmo trova min
look_up_table = {dato.x-dato.inc_x: dato for dato in dati if dato.inc_x >= threshold}
look_keys = list(look_up_table.keys())
min_key = look_up_table[max(look_keys)]
coeff_min = min_key.y/(min_key.x-min_key.inc_x)
inc_coeff_min = (min_key.inc_x/min_key.x + min_key.inc_y/min_key.y) * coeff_min
#algoritmo trova max
look_up_table = {dato.x+dato.inc_x: dato for dato in dati if dato.inc_x >= threshold}
look_keys = list(look_up_table.keys())
min_key = look_up_table[min(look_keys)]
coeff_max = min_key.y/(min_key.x+min_key.inc_x)
inc_coeff_max = (min_key.inc_x/min_key.x + min_key.inc_y/min_key.y) * coeff_max
#retta di fit
coeff_fit = (coeff_max+coeff_min)/2
#mettere a schermo i coefficenti
print(f'{coeff_max} , {inc_coeff_max}')
print(f'{coeff_min} , {inc_coeff_min}')
print(f'{coeff_fit} , {abs(coeff_max-coeff_min)/2}')
#print(coeff)
print(1/coeff_inv[0])
print(coeff_inv[1])
#aggiunge le rette ai punti
retta_max = math_function(coeff_max , dati_x)
ax.plot(retta_max[0] , retta_max[1] , "--" , label="retta di massima pendenza")
retta_min = math_function(coeff_min , dati_x)
ax.plot(retta_min[0] , retta_min[1] , "--" , label="retta di minima pendenza")
retta_fit = math_function(coeff_fit , dati_x)
ax.plot(retta_fit[0] , retta_fit[1] , "" , label="retta di fit")
#aggiunge etichetta ai punti
for h in dati:
    text = f'{h.name}'
    x = h.x
    y = h.y
    dist_x = h.dist_x
    dist_y = h.dist_y
    inc_y_int = h.inc_y
    p = 0
    if inc_y_int > 0.5:
        p = 10
    plt.annotate(text,(x+dist_x,y+dist_y),textcoords="offset points",xytext=(0,0),ha='center')

plt.xlim(0 , m.ceil(max(dati_x) + max(inc_x_0)*2))
plt.ylim(0 , m.ceil(max(dati_y) + max(inc_y)*2000))
plt.ylabel("massa (g)")
plt.xlabel("volume (cm^3)")
#plt.legend(["valore medio dato" , "incertezza dato" , "retta del migliore chi^2" , "retta della media pesata"] , loc="upper left")
plt.legend(loc="upper left")
plt.show()