
# Definición de función
def suma(a, b):
    return a+b

def resta(z,m):
    return z-m

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


if __name__ == '__main__':
    x=5
    y=10
    print( suma(x,y)     )

    print(resta(x,y))

    print(suma(123,456))    

    if x>y:
        print("x es mayor que y")
    else:
        print("x puede ser igual a y o y mayor que x")