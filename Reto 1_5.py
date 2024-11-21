def id_letras(palabras:list):
    palab=palabras.copy()
    for i in range(len(palab)):
        palab[i]=palab[i].lower()
        palab[i]=''.join(sorted(palab[i]))
    repet=[]
    unic=[]
    for i in range(len(palab)):
        if palab[i] in unic:
            unic.remove(palab[i])
            repet.append(palab[i])
        else:
            unic.append(palab[i])
    apar=[]
    for i in range(len(repet)):
        lista=[]
        while repet[i] in palab:
            ind=palab.index(repet[i])
            lista.append(palabras[ind])
            palab[ind]=" "
        if len(lista)>2:
            apar.append(lista)
    return apar

if __name__=="__main__":
    l_lista=int(input("De cuantas palabras quiere su lista: "))
    palabras=[]
    for i in range(l_lista):
        palabras.append(input(f"Ingrese la palabra {i+1}: "))
    apar=id_letras(palabras)
    for i in apar:
        print(i)