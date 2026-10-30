if __name__ == '__main__':
    #notas [0,10]
    maximo=-1
    minimo=11

    for i in range(1,6):
        nota=float(input("Dime la nota "))
        
        if (nota>maximo):maximo=nota

        if (nota<minimo):minimo=nota

    print(f'maximo:{maximo}\nminimo:{minimo}')



