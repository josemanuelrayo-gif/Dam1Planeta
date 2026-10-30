import random

def imprimir():
    global lista
    for i in range(0,len(lista)):
        print(f'{i} {lista[i]}')

if __name__ == '__main__':
    lista=[]

    for i in range(1,21):
        lista.append(random.randint(50,200))
    
    imprimir()

