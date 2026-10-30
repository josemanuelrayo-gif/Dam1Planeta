import math



def binarioAdecimal(cadena):
    #cadena 111
    n=len(cadena)-1
    j=0
    suma=0
    for i in range(n,-1,-1):
        suma +=int(cadena[i])*math.pow(2,j)
        j+=1
    return suma    

def decimalAbinario(numero):
    binario=""
    while(numero>0):
        resto=numero%2
        binario =str(resto)+binario
        numero=numero//2
    return binario



if __name__ == '__main__':
    #n=int(input("Dime el numero decimal "))
    #print(decimalAbinario(n))
    print(binarioAdecimal("111"))


