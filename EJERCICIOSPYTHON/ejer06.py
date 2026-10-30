n=int(input("Dime el nº de mes"))
print(n)

print(n,((n-1)//3)+1)
print(n,((n-1)//6)+1)

if not(n>=1 and n<=12):
    print("El numero de mes tiene que estar entre 1 y 12")    
elif n<=3:
    print("Primer trimestre")    
elif n<=6:
    print("Segundo trimestre")        
elif n<=9:
    print("Tercer trimestre")        
else:
    print("Cuarto trimestre")            

print("final del progrma")

