from os import system
system("cls")


#base 2*2*2*2
#expo 4-3-2-1
def potencia(b:int, exp:int)->int:
    if exp==0:
        return 1
    
    return b*potencia(b, exp-1)



base=int(input("Ingrese base:"))
expo=int(input("Ingrese exponente:"))

print(f"La pontencia de {base} elevado a {expo} es {potencia(base,expo)}")