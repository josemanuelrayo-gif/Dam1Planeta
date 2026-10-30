import math

def decimalAbinario(n):
    binario=""
    while(n>0):
        resto=n%2
        binario=str(resto)+binario
        n=n//2
    return binario

def decimalAHexadecimal(n):
    ca="0123456789ABCDEF"
    binario=""
    while(n>0):
        resto=n%16
        binario=ca[resto:resto+1]+binario
        n=n//16
    return binario

def HexadecimalAdecimal(cadena):
    # FF
    ca="0123456789ABCDEF"
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma +=ca.find(cadena[i:i+1])*math.pow(16,j)
        j+=1
    return suma



def decimalAOctal(n):
    binario=""
    while(n>0):
        resto=n%8
        binario=str(resto)+binario
        n=n//8
    return binario


if __name__ == '__main__':
    
    print(HexadecimalAdecimal("FF"))
    
    while(True):
        n=int(input("Dime el numero "))
        if (n<0): break
        print(decimalAbinario(n))
        print(decimalAHexadecimal(n))
        print(decimalAOctal(n))