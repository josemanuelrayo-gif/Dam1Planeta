def reverso(cadena):
    salida=""
    for i in range(len(cadena)-1,-1,-1):
        salida +=cadena[i]
    return salida

def letradni(numero):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"
    n=numero%23
    return cadena[n]

def letranie(texto):
    #Z5034722 ----->G
    texto=str("XYZ".index(texto[0]))+texto[1:]
    return letradni(int(texto))
    
def letraniedni(texto):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"

    n="XYZ".find(texto[0])

    if (n==-1):
        m=int(texto)%23
    else:
        m=int(str(n)+texto[1:])%23

    return cadena[m]        

if __name__ == '__main__':
    dni="50691319"
    print(dni,letraniedni(dni))

    nie="Z5034722"
    print(nie,letraniedni(nie))

    print(reverso("Hasta mañana a las 8"))