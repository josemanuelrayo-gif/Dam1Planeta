import math

def soluciones(a,b,c):
    discriminante=math.pow(b,2)-(4*a*c) 

    if (discriminante<0):
        print("No hay soluciones")
    elif (discriminante==0):
        print(f"La raiz es { -b/(2*a) }")
    else:
        x1=  (-b+math.sqrt(discriminante))/(2*a)  
        x2=  (-b-math.sqrt(discriminante))/(2*a)  
        print(f'las raices son {x1} y {x2}')


if __name__ == '__main__':
    # ax^2+bx+c=0
    va=float(input("Dime el coeficiente a "))
    vb=float(input("Dime el coeficiente b "))
    vc=float(input("Dime el coeficiente c "))
    
    soluciones(va,vb,vc)


    