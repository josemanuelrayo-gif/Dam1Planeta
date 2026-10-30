def metodo():
    global lista,pares,impares
    for i in range(0,len(lista)):
        if (lista[i]%2==0):
            pares.append(lista[i])
        else:
            impares.append(lista[i])    


if __name__ == '__main__':
    lista=[2,5,8,11,3,7]
    pares=[]
    impares=[]
    metodo()
    print(pares)
    print(impares)