
def reverso(n):
    resultado=0
    while(n>0):
        resto=n%10
        resultado=(resultado*10)+resto
        n =n//10
    return resultado    

if __name__ == '__main__':
    m=int(input("Dime el nº "))
    digito=int(input("Dime el digito "))
    n=reverso(m)
    c=0
    while(n>0):
        resto=n%10
        c +=1
        if (resto==digito):
            print(c,end=" ")
        n=n//10
   
