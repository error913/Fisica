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


r1 = Point("10±2","97,80±0,04" ,"r1" , 0 , 0)
r2 = Point("7±2", "55,50±0,04","r2",0 , 0)
r3 = Point("7±2","62,20±0,04" ,"r3",0 , 0)
c1 = Point("9±2","76,42±0,04" ,"c1",0 , 0)
c2 = Point("11±2", "101,37±0,04","c2",0 , 0)
c3 = Point("20±2", "184,05±0,04","c3",0 , 0)
r1_b = Point("11,5	±	0,2","97,99	±	0,01", "r1" , 0 , -10)
r2_b = Point("6,8	±	0,1","55,56	±	0,01" ,"r2"  ,0 , -8)
r3_b = Point("7,2	±	0,1" ,"62,31	±	0,01","r3" , 0 , 8)
c1_b = Point("4,7	±	0,1" ,"76,57	±	0,01","c1" , 0 ,5 )
c2_b = Point("11	±	0,2" ,"101,51	±	0,01","c2",0 , 5)
c3_b = Point("23	±	0,2","184,14	±	0,01" ,"c3" , 0 , -8)

dati = [r1 , r2 , r3 , c1 , c2 , c3 , r1_b , r2_b , r3_b , c1_b , c2_b , c3_b]
dati_x = [h.x for h in dati]
dati_y = [h.y for h in dati]
inc_x_0 = [h.inc_x for h in dati]
inc_y = [h.inc_y for h in dati]
dens =  8.91
print((chi.sum_chi(dati_y[0:3] , dati_x[0:3] , inc_x_0[0:3] , dens)+chi.sum_chi(dati_y[3:7] , dati_x[3:7] , inc_x_0[3:7] , dens))/2)