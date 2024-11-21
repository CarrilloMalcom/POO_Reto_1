
def main():
    print("Ingrese sus numeros y la operación que quiere aplicarles")
    a=int(input("Ingrese su primer entero"))
    b=int(input("Ingrese su segundo entero"))
    op=input("Ingrese la operación que quiere aplicar (símbolo: +, -, /, *)")
    match op:
        case "+":
            res=a+b
        case "-":
            res=a-b
        case "*":
            res=a*b
        case "/":
            res=a/b
        case _:
            print("No se ha ingresado una operación valida")
            main()
    return a, b, op, res
if __name__=="__main__":
    a, b, op, res=main()
    print(f"El resultado de {a} {op} {b} es {res}")
