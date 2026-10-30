import random

def añadir():
    global lista
    for i in range(20):
        n=random.randint(10,50)
        lista.append(n)
        #print(f'{i+1} {n}')

def calcular():
    global lista
    maximo=minimo=cmaximo=cminimo=suma=0

    for i in range(len(lista)):
        suma +=lista[i]
        if (i==0):
            maximo=minimo=lista[i]
            cmaximo=cminimo=1
        else:
            #========================
            if (lista[i]>maximo):
                maximo=lista[i]
                cmaximo=1
            elif (lista[i]==maximo):        
                cmaximo +=1
            #========================
            if (lista[i]<minimo):
                minimo=lista[i]
                cminimo=1
            elif (lista[i]==minimo):        
                cminimo +=1    
    
    print(f'La media es {suma/len(lista):.2f}')
    print(f'Maximo: {maximo} y el nº veces {cmaximo}')
    print(f'Minimo: {minimo} y el nº veces {cminimo}')



if __name__ == '__main__':
    lista=[]
    añadir()
    print(lista.sort())
    print(lista)
    calcular()