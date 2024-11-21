def palindromo(palabra:int)->str:
    pal_char=list(palabra)
    inv_pal_char=[]
    for i in range(len(pal_char)):
        inv_pal_char.insert(0, pal_char[i])
    return pal_char==inv_pal_char

if __name__=="__main__":
    palabra=input()
    pal=palindromo(palabra)
    if pal:
        print(f"la palabra {palabra} es un palindromo")
    else:
        print(f"la palabra {palabra} NO es un palindromo")