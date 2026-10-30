




if __name__ == '__main__':
    n=int(input("Dime el nº de numeros "))
    suma=0
    for i in range(1,n+1):
        numero=float(input(f'Dime el nº {i} '))
        suma +=numero  #suma =suma+numero

        if (i==1):
            maximo=minimo=numero
            cmaximo=cminimo=1
        else:
            if (numero>maximo):
                maximo=numero
                cmaximo=1
            elif (numero==maximo):
                cmaximo +=1 # cmaximo=cmaximo+1

            if (numero<minimo):
                minimo=numero
                cminimo=1
            elif (numero==minimo):
                cminimo +=1 # cminimo=cminimo+1

    print(f'La media es {suma/n:.2f}')
    print(f'Maximo:{maximo} y nº veces {cmaximo}')
    print(f'Minimo:{minimo} y nº veces {cminimo}')        

        

           
                
