def primo(numero:int):
    limite=(int(numero/2)+1)
    for i in range(2, limite):
        if numero%i==0:
            return False
    return True

if __name__=="__main__":
    l_lista=int(input("De cuantos numeros quiere su lista: "))
    lista=[]
    for i in range(l_lista):
        lista.append(int(input(f"Ingrese el numero {i+1}: ")))
    primos=[]
    for i in lista:
        if primo(i):
            primos.append(i)
    print(f"Los numeros primos de la lista de numeros dados son: \n{primos}")