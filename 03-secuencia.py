from os import system
system("cls")

def suma(valor:int)->int:
    if valor==0:
        return 0
    
    return valor+suma(valor-1)


n=3
print(f"El valor de la {n} es {suma(n)}")

