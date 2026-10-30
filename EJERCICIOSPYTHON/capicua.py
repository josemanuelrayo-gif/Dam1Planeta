
def reverso(n):
    resultado=0
    while(n>0):
        resto=n%10
        resultado=(resultado*10)+resto
        n =n//10
    return resultado    





if __name__ == '__main__':
    numero=int(input("Dime un numero "))

    if (numero==reverso(numero)):
        print("Capicua")
    else:
        print("No Capicua")    
