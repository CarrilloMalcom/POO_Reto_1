def mayor_suma(numeros: list):
    mayor=0
    elementos=[0, 0]
    index=[0, 0]
    for i in range(len(numeros)-1):
        sum=numeros[i]+numeros[i+1]
        if sum>mayor:
            mayor=sum
            elementos[0], elementos[1]=numeros[i], numeros[i+1]
            index[0], index[1]=i+1, i+2
    return mayor, elementos, index

if __name__=="__main__":
    l_lista=int(input("De cuantos numeros quiere su lista: "))
    numeros=[]
    for i in range(l_lista):
        numeros.append(int(input(f"Ingrese el numero {i+1}: ")))
    mayor, elementos, index=mayor_suma(numeros)
    print(f"De la lista {numeros} 
          \nla mayor suma posible de consecutivos es: {mayor} 
           \nde los elementos{elementos} 
           \nen las posiciones {index}")