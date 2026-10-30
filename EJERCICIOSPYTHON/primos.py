def isPrimo(n):
    for i in range(2,n):
        if (n%i==0): return False
    return True


if __name__ == '__main__':
    numero=int(input("Dime el nº a partir del cual  ?"))
    c=0
    while(c<5):
        if (isPrimo(numero)):
            c+=1
            print(f'{c} {numero} ') 
        numero+=1

