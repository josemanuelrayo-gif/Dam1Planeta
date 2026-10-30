




if __name__ == '__main__':
    #campo de existencia -&,+&

    for i in range(1,6):
        numero=float(input("Introduce el nº"))
        if (i==1):
            maximo=minimo=numero
        else:
            if (numero>maximo):
                maximo=numero
            elif (numero<minimo):
                minimo=numero
    
    print(f'El mínimo:{minimo}\nEl máximo:{maximo}')






