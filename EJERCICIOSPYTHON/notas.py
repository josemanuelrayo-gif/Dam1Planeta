nota=float(input("Dime el nº de nota "))


if (nota<0 or nota>10):
    mensaje="Fuera de rango"
elif (nota<5):
    mensaje="Suspenso"
elif (nota<6):
    mensaje="Aprobado"
elif (nota<7):
    mensaje="Bien"
elif (nota<9):
    mensaje="Notable"
else :
    mensaje="Sobresaliente"

print(mensaje)