mes=int(input("Dime el nº de mes (1-12) "))
dia=int(input("Dime el nº de día dentro del mes "))

fecha=(mes*100)+dia

#Capricornio: 22 de diciembre al 19 de enero.
#Acuario: 20 de enero al 18 de febrero
#Piscis: 19 de febrero al 20 de marzo
#Aries: 21 de marzo al 19 de abril.
#Tauro: 20 de abril al 20 de mayo.
#Géminis: 21 de mayo al 20 de junio.
#Cáncer: 21 de junio al 22 de julio.
#Leo: 23 de julio al 22 de agosto.
#Virgo: 23 de agosto al 22 de septiembre.
#Libra: 23 de septiembre al 22 de octubre.
#Escorpio: 23 de octubre al 21 de noviembre.
#Sagitario: 22 de noviembre al 21 de diciembre.

if ((fecha>=1222 and fecha<=1231) or (fecha>=101 and fecha<=119)):
    signo="Capricornio"
elif ( fecha>=120 and fecha<=218):
    signo="Acuario"
elif ( fecha>=219 and fecha<=320):
    signo="Piscis"
elif ( fecha>=321 and fecha<=419):
    signo="Aries"
elif ( fecha>=420 and fecha<=520):
    signo="Tauro"
elif ( fecha>=421 and fecha<=620):
    signo="Géminis"
elif ( fecha>=621 and fecha<=722):
    signo="Cáncer"
elif ( fecha>=723 and fecha<=822):
    signo="Leo"
elif ( fecha>=823 and fecha<=922):
    signo="Virgo"
elif ( fecha>=923 and fecha<=1022):
    signo="Libra"
elif ( fecha>=1023 and fecha<=1121):
    signo="Escorpio"
elif ( fecha>=1122 and fecha<=1221):
    signo="Sagitario"
else:
    signo="Fuera de rango" 


print(signo)