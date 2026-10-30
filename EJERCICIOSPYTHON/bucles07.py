



if __name__ == '__main__':
    cpares=cimpares=0

    while(True):
        n=int(input("Introduce un numero "))
        if (n<0):break
        if (n%2==0):
            cpares +=1
        else:
            cimpares +=1

    print(f'Nº de pares: {cpares}\n Nº de impares: {cimpares} ')    
